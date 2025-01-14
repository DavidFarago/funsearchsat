# Copyright 2023 DeepMind Technologies Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Class for sampling new programs."""
from collections.abc import Collection, Sequence

import numpy as np
from llama_cpp import Llama
from funsearch.implementation import evaluator
from funsearch.implementation import programs_database


CTX = 2048

class LLM:
  """Language model (see https://huggingface.co/TheBloke/phi-2-GGUF) that predicts continuation of provided source code."""

  def __init__(self, samples_per_prompt: int) -> None:
    self._samples_per_prompt = samples_per_prompt
    self.llm = Llama(
      model_path="./phi-2.Q4_K_M.gguf",  # Download the model file first, "phi-2.Q4_K_M.gguf" is "medium, balanced quality - recommended"
      n_ctx=CTX,  # The max sequence length to use - note that longer sequence lengths require much more resources
      n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance
      n_gpu_layers=35         # The number of layers to offload to GPU, if you have GPU acceleration available. Set to 0 if no GPU acceleration
    )

  def _draw_sample(self, prompt: str) -> str:
    """Returns a predicted continuation of `prompt`."""
    return self.llm(
      "Instruct: {prompt}\nOutput:", 
      max_tokens=CTX // 3,
      stop=["<|endoftext|>"],
      echo=False,
    )

  def draw_samples(self, prompt: str) -> Collection[str]:
    """Returns multiple predicted continuations of `prompt`."""
    return [self._draw_sample(prompt) for _ in range(self._samples_per_prompt)]


class Sampler:
  """Node that samples program continuations and sends them for analysis."""

  def __init__(
      self,
      database: programs_database.ProgramsDatabase,
      evaluators: Sequence[evaluator.Evaluator],
      samples_per_prompt: int,
  ) -> None:
    self._database = database
    self._evaluators = evaluators
    self._llm = LLM(samples_per_prompt)

  def sample(self):
    """Continuously gets prompts, samples programs, sends them for analysis."""
    while True:
      prompt = self._database.get_prompt()
      samples = self._llm.draw_samples(prompt.code)
      # This loop can be executed in parallel on remote evaluator machines.
      for sample in samples:
        chosen_evaluator = np.random.choice(self._evaluators)
        chosen_evaluator.analyse(
            sample, prompt.island_id, prompt.version_generated)
