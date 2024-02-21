
# BCE Options
## blocked clause elimination
### def: 0, min: 0, max: 1
def block(featrec):
    return 0
## maximum clause size
### def: 1e5, min: 1, max: 2e9
def blockmaxclslim(featrec):
    return 1e5
## minimum clause size
### def: 2, min: 2, max: 2e9
def blockminclslim(featrec):
    return 2
## occurrence limit
### def: 1e2, min: 1, max: 2e9
def blockocclim(featrec):
    return 1e2

# Covered Clause Elimination Options
## covered clause elimination
### def: 0, min: 0, max: 1
def cover(featrec):
    return 0
## maximum clause size
### def: 1e5, min: 1, max: 2e9
def covermaxclslim(featrec):
    return 1e5
## maximum cover efficiency
### def: 1e8, min: 0, max: 2e9
def covermaxeff(featrec):
    return 1e8
## minimum clause size
### def: 2, min: 2, max: 2e9
def coverminclslim(featrec):
    return 2
## minimum cover efficiency
### def: 1e6, min: 0, max: 2e9
def covermineff(featrec):
    return 1e6
## relative efficiency per mille
### def: 4, min: 1, max: 1e5
def coverreleff(featrec):
    return 4

# Decompose Options
## decompose BIG in SCCs and ELS
### def: 1, min: 0, max: 1
def decompose(featrec):
    return 1
## number of decompose rounds
### def: 2, min: 1, max: 16
def decomposerounds(featrec):
    return 2

# Elimination Options
## bounded variable elimination
### def: 1, min: 0, max: 1
def elim(featrec):
    return 1
## find AND gates
### def: 1, min: 0, max: 1
def elimands(featrec):
    return 1
## maximum elimination efficiency
### def: 2e9, min: 0, max: 2e9
def elimaxeff(featrec):
    return 2e9
## eager backward subsumption
### def: 1, min: 0, max: 1
def elimbackward(featrec):
    return 1
## maximum elimination bound
### def: 16, min: -1, max: 2e6
def elimboundmax(featrec):
    return 16
## minimum elimination bound
### def: 0, min: -1, max: 2e6
def elimboundmin(featrec):
    return 0
## resolvent size limit
### def: 1e2, min: 2, max: 2e9
def elimclslim(featrec):
    return 1e2
## find equivalence gates
### def: 1, min: 0, max: 1
def elimequivs(featrec):
    return 1
## minimum elimination efficiency
### def: 1e7, min: 0, max: 2e9
def elimineff(featrec):
    return 1e7
## elimination interval
### def: 2e3, min: 1, max: 2e9
def elimint(featrec):
    return 2e3
## find if-then-else gates
### def: 1, min: 0, max: 1
def elimites(featrec):
    return 1
## limit resolutions
### def: 1, min: 0, max: 1
def elimlimited(featrec):
    return 1
## occurrence limit
### def: 1e2, min: 0, max: 2e9
def elimocclim(featrec):
    return 1e2
## elim score product weight
### def: 1, min: 0, max: 1e4
def elimprod(featrec):
    return 1
## relative efficiency per mille
### def: 1e3, min: 1, max: 1e5
def elimreleff(featrec):
    return 1e3
## usual number of rounds
### def: 2, min: 1, max: 512
def elimrounds(featrec):
    return 2
## elimination by substitution
### def: 1, min: 0, max: 1
def elimsubst(featrec):
    return 1
## elimination score sum weight
### def: 1, min: 0, max: 1e4
def elimsum(featrec):
    return 1
## maximum XOR size
### def: 5, min: 2, max: 27
def elimxorlim(featrec):
    return 5
## find XOR gates
### def: 1, min: 0, max: 1
def elimxors(featrec):
    return 1

# Instantiate Options
## variable instantiation
### def: 0, min: 0, max: 1
def instantiate(featrec):
    return 0
## minimum clause size
### def: 3, min: 2, max: 2e9
def instantiateclslim(featrec):
    return 3
## maximum occurrence limit
### def: 1, min: 1, max: 2e9
def instantiateocclim(featrec):
    return 1
## instantiate each clause once
### def: 1, min: 0, max: 1
def instantiateonce(featrec):
    return 1

# Failed Literal Probing Options
## failed literal probing
### def: 1, min: 0, max: 1
def probe(featrec):
    return 1
## learn hyper binary clauses
### def: 1, min: 0, max: 1
def probehbr(featrec):
    return 1
## probing interval
### def: 5e3, min: 1, max: 2e9
def probeint(featrec):
    return 5e3
## maximum probing efficiency
### def: 1e8, min: 0, max: 2e9
def probemaxeff(featrec):
    return 1e8
## minimum probing efficiency
### def: 1e6, min: 0, max: 2e9
def probemineff(featrec):
    return 1e6
## relative efficiency per mille
### def: 20, min: 1, max: 1e5
def probereleff(featrec):
    return 20
## probing rounds
### def: 1, min: 1, max: 16
def proberounds(featrec):
    return 1

# Clause Subsumption Options
## clause subsumption
### def: 1, min: 0, max: 1
def subsume(featrec):
    return 1
## watch list length limit
### def: 1e4, min: 0, max: 2e9
def subsumebinlim(featrec):
    return 1e4
## clause length limit
### def: 1e2, min: 0, max: 2e9
def subsumeclslim(featrec):
    return 1e2
## subsume interval
### def: 1e4, min: 1, max: 2e9
def subsumeint(featrec):
    return 1e4
## limit subsumption checks
### def: 1, min: 0, max: 1
def subsumelimited(featrec):
    return 1
## maximum subsuming efficiency
### def: 1e8, min: 0, max: 2e9
def subsumemaxeff(featrec):
    return 1e8
## minimum subsuming efficiency
### def: 1e6, min: 0, max: 2e9
def subsumemineff(featrec):
    return 1e6
## watch list length limit
### def: 1e2, min: 0, max: 2e9
def subsumeocclim(featrec):
    return 1e2
## relative efficiency per mille
### def: 1e3, min: 1, max: 1e5
def subsumereleff(featrec):
    return 1e3
## strengthen during subsume
### def: 1, min: 0, max: 1
def subsumestr(featrec):
    return 1

# Hyper Ternary Resolution Options
## hyper ternary resolution
### def: 1, min: 0, max: 1
def ternary(featrec):
    return 1
## max clauses added in percent
### def: 1e3, min: 0, max: 1e4
def ternarymaxadd(featrec):
    return 1e3
## maximum efficiency
### def: 1e8, min: 0, max: 2e9
def ternarymaxeff(featrec):
    return 1e8
## minimum efficiency
### def: 1e6, min: 1, max: 2e9
def ternarymineff(featrec):
    return 1e6
## ternary occurrence limit
### def: 1e2, min: 1, max: 2e9
def ternaryocclim(featrec):
    return 1e2
## relative efficiency per mille
### def: 10, min: 1, max: 1e5
def ternaryreleff(featrec):
    return 10
## maximum ternary rounds
### def: 2, min: 1, max: 16
def ternaryrounds(featrec):
    return 2

# Transitive Reduction Options
## transitive reduction of BIG
### def: 1, min: 0, max: 1
def transred(featrec):
    return 1
## maximum efficiency
### def: 1e8, min: 0, max: 2e9
def transredmaxeff(featrec):
    return 1e8
## minimum efficiency
### def: 1e6, min: 0, max: 2e9
def transredmineff(featrec):
    return 1e6
## relative efficiency per mille
### def: 1e2, min: 1, max: 1e5
def transredreleff(featrec):
    return 1e2

# Vivification Options
## vivification
### def: 1, min: 0, max: 1
def vivify(featrec):
    return 1
## instantiate last literal when vivify
### def: 1, min: 0, max: 1
def vivifyinst(featrec):
    return 1
## maximum efficiency
### def: 2e7, min: 0, max: 2e9
def vivifymaxeff(featrec):
    return 2e7
## minimum efficiency
### def: 2e4, min: 0, max: 2e9
def vivifymineff(featrec):
    return 2e4
## vivify once: 1=red, 2=red+irr
### def: 0, min: 0, max: 2
def vivifyonce(featrec):
    return 0
## redundant efficiency per mille
### def: 75, min: 0, max: 1e3
def vivifyredeff(featrec):
    return 75
## relative efficiency per mille
### def: 20, min: 1, max: 1e5
def vivifyreleff(featrec):
    return 20

####################################################################

# Compact Options
## compact internal variables
### def: 1, min: 0, max: 1
def compact(featrec):
    return 1
## compacting interval
### def: 2e3, min: 1, max: 2e9
def compactint(featrec):
    return 2e3
## inactive limit per mille
### def: 1e2, min: 0, max: 1e3
def compactlim(featrec):
    return 1e2
## minimum inactive limit
### def: 1e2, min: 1, max: 2e9
def compactmin(featrec):
    return 1e2

# Deduplicate Options
## remove duplicated binaries
### def: 1, min: 0, max: 1
def deduplicate(featrec):
    return 1


def getoptdict(featrec):
    return {
        # BCE Options, off by default
        "--block": block(featrec),
        "--blockmaxclslim": blockmaxclslim(featrec),
        "--blockminclslim": blockminclslim(featrec),
        "--blockocclim": blockocclim(featrec),
        # CCE Options, off by default
        "--cover": cover(featrec),
        "--covermaxclslim": covermaxclslim(featrec),
        "--covermaxeff": covermaxeff(featrec),
        "--coverminclslim": coverminclslim(featrec),
        "--covermineff": covermineff(featrec),
        "--coverreleff": coverreleff(featrec),
        # Instantiate Options, off by default
        "--instantiate": instantiate(featrec),
        "--instantiateclslim": instantiateclslim(featrec),
        "--instantiateocclim": instantiateocclim(featrec),
        "--instantiateonce": instantiateonce(featrec),
        # Vivification Options, on by default
        "--vivify": vivify(featrec),
        "--vivifyinst": vivifyinst(featrec),
        "--vivifymaxeff": vivifymaxeff(featrec),
        "--vivifymineff": vivifymineff(featrec),
        "--vivifyonce": vivifyonce(featrec),
        "--vivifyredeff": vivifyredeff(featrec),
        "--vivifyreleff": vivifyreleff(featrec),
        # BVE Options, on by default
        "--elim": elim(featrec),
        "--elimands": elimands(featrec),
        "--elimmaxeff": elimaxeff(featrec),
        "--elimbackward": elimbackward(featrec),
        "--elimboundmax": elimboundmax(featrec),
        "--elimboundmin": elimboundmin(featrec),
        "--elimclslim": elimclslim(featrec),
        "--elimequivs": elimequivs(featrec),
        "--elimineff": elimineff(featrec),
        "--elimint": elimint(featrec),
        "--elimites": elimites(featrec),
        "--elimlimited": elimlimited(featrec),
        "--elimocclim": elimocclim(featrec),
        "--elimprod": elimprod(featrec),
        "--elimreleff": elimreleff(featrec),
        "--elimrounds": elimrounds(featrec),
        "--elimsubst": elimsubst(featrec),
        "--elimsum": elimsum(featrec),
        "--elimxorlim": elimxorlim(featrec),
        "--elimxors": elimxors(featrec),
        # Clause Subsumption Options, on by default
        "--subsume": subsume(featrec),
        "--subsumebinlim": subsumebinlim(featrec),
        "--subsumeclslim": subsumeclslim(featrec),
        "--subsumeint": subsumeint(featrec),
        "--subsumelimited": subsumelimited(featrec),
        "--subsumemaxeff": subsumemaxeff(featrec),
        "--subsumemineff": subsumemineff(featrec),
        "--subsumeocclim": subsumeocclim(featrec),
        "--subsumereleff": subsumereleff(featrec),
        "--subsumestr": subsumestr(featrec),
        # Failed Literal Probing Options, on by default
        "--probe": probe(featrec),
        "--probehbr": probehbr(featrec),
        "--probeint": probeint(featrec),
        "--probemaxeff": probemaxeff(featrec),
        "--probemineff": probemineff(featrec),
        "--probereleff": probereleff(featrec),
        "--proberounds": proberounds(featrec),
        # Hyper Ternary Resolution Options, on by default
        "--ternary": ternary(featrec),
        "--ternarymaxadd": ternarymaxadd(featrec),
        "--ternarymaxeff": ternarymaxeff(featrec),
        "--ternarymineff": ternarymineff(featrec),
        "--ternaryocclim": ternaryocclim(featrec),
        "--ternaryreleff": ternaryreleff(featrec),
        "--ternaryrounds": ternaryrounds(featrec),
        # Transitive Reduction Options, on by default
        "--transred": transred(featrec),
        "--transredmaxeff": transredmaxeff(featrec),
        "--transredmineff": transredmineff(featrec),
        "--transredreleff": transredreleff(featrec),
        # Decompose, Compact and Deduplicate Options, do not tune this
        "--decompose": decompose(featrec),
        "--decomposerounds": decomposerounds(featrec),
        "--compact": compact(featrec),
        "--compactint": compactint(featrec),
        "--compactlim": compactlim(featrec),
        "--compactmin": compactmin(featrec),
        "--deduplicate": deduplicate(featrec)
    }