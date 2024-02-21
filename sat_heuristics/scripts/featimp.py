#!/usr/bin/env python

from gbd_core.api import GBD
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
def main():
    with GBD([ 'sat_heuristics/scripts/gbd/meta.db', 'sat_heuristics/scripts/gbd/base.db' ]) as gbd:
        feat = gbd.get_features('base_db')
        data = gbd.query("base_features_runtime != memout", resolve=feat + [ 'family' ])
        
        X = data[feat]
        y = data['family']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy:", accuracy)

        feature_importances = model.feature_importances_
        feature_names = X.columns
        sorted_features = sorted(zip(feature_names, feature_importances), key=lambda x: x[1], reverse=True)
        print("Features sorted by importance:")
        for feature_name, importance in sorted_features:
            print("{} {:.2f}".format(feature_name, importance))

        subsets = {
            'top5': [ name for (name, _) in sorted_features[:5] ],
            'top10': [ name for (name, _) in sorted_features[:10] ],
            'top15': [ name for (name, _) in sorted_features[:15] ],
            'clauseType': ['clauses', 'variables', 'cls1', 'cls2', 'cls3', 'cls4', 'cls5', 'cls6', 'cls7',  'cls8', 'cls9', 'cls10p', 'horn', 'invhorn', 'positive', 'negative'],
            'hornVarDist': ['hornvars_mean', 'hornvars_variance', 'hornvars_min', 'hornvars_max', 'hornvars_entropy', 'invhornvars_mean', 'invhornvars_variance', 'invhornvars_min', 'invhornvars_max', 'invhornvars_entropy'],
            'posNegBalanceDist': ['balancecls_mean', 'balancecls_variance', 'balancecls_min', 'balancecls_max', 'balancecls_entropy', 'balancevars_mean', 'balancevars_variance', 'balancevars_min', 'balancevars_max', 'balancevars_entropy'],
            'vcgDist': ['vcg_vdegree_mean', 'vcg_vdegree_variance', 'vcg_vdegree_min', 'vcg_vdegree_max', 'vcg_vdegree_entropy', 'vcg_cdegree_mean', 'vcg_cdegree_variance', 'vcg_cdegree_min', 'vcg_cdegree_max', 'vcg_cdegree_entropy'],
            'vgcgDist': ['vg_degree_mean', 'vg_degree_variance', 'vg_degree_min', 'vg_degree_max', 'vg_degree_entropy', 'cg_degree_mean', 'cg_degree_variance', 'cg_degree_min', 'cg_degree_max', 'cg_degree_entropy']
        }

        # Train and evaluate model for each feature list
        for name, list in subsets.items():
            X_train_feature = X_train[list]
            X_test_feature = X_test[list]
            model_feature = RandomForestClassifier()
            model_feature.fit(X_train_feature, y_train)
            y_pred_feature = model_feature.predict(X_test_feature)
            accuracy_feature = accuracy_score(y_test, y_pred_feature)
            print(f"Accuracy with {name} features:", accuracy_feature)
            feature_importances = model_feature.feature_importances_
            sorted_features = sorted(zip(list, feature_importances), key=lambda x: x[1], reverse=True)
            print("Features sorted by importance:")
            for feature_name, importance in sorted_features:
                print("{} {:.2f}".format(feature_name, importance))
       

if __name__ == "__main__":
    main()