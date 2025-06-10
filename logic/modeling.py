from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.svm import SVC, SVR
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import accuracy_score, mean_squared_error, confusion_matrix, classification_report, silhouette_score
import pandas as pd
import numpy as np

def build_models(df, target_column):
    import warnings
    warnings.filterwarnings("ignore")

    X = df.drop(columns=[target_column])
    y = df[target_column]

    if y.dtype == 'object' or y.dtype.name == 'category':
        is_classification = True
    elif np.issubdtype(y.dtype, np.number):
        if len(y.unique()) <= 3:
            is_classification = True
        else:
            is_classification = False
    else:
        is_classification = False

    if is_classification and not np.issubdtype(y.dtype, np.integer):
        y = y.round().astype(int)

    supervised_models = {
        "Decision Tree": DecisionTreeClassifier() if is_classification else DecisionTreeRegressor(),
        "Random Forest": RandomForestClassifier() if is_classification else RandomForestRegressor(),
        "SVM": SVC(probability=True) if is_classification else SVR(),
        "K-Nearest Neighbors": KNeighborsClassifier() if is_classification else KNeighborsRegressor(),
        "Naive Bayes": GaussianNB() if is_classification else None,
    }

    if is_classification:
        supervised_models["Logistic Regression"] = LogisticRegression(max_iter=1000)

    unsupervised_models = {
        "K-Means Clustering": KMeans(n_clusters=5, random_state=42),
        "DBSCAN": DBSCAN(eps=0.5, min_samples=5),
        "Agglomerative Clustering": AgglomerativeClustering(n_clusters=5)
    }

    results = {
        "supervised": [],
        "unsupervised": []
    }

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    for name, model in supervised_models.items():
        if model is None:
            results["supervised"].append({
                "model": name,
                "error": "Not supported for regression tasks."
            })
            continue

        try:
            model.fit(X_train, y_train)
            preds = model.predict(X_test)

            if is_classification:
                from sklearn.metrics import precision_score, recall_score, f1_score

                results["supervised"].append({
                    "model": name,
                    "type": "classification",
                    "accuracy": accuracy_score(y_test, preds),
                    "precision": precision_score(y_test, preds, average='weighted', zero_division=0),
                    "recall": recall_score(y_test, preds, average='weighted', zero_division=0),
                    "f1_score": f1_score(y_test, preds, average='weighted', zero_division=0),
                    "confusion_matrix": confusion_matrix(y_test, preds)
                })
            else:
                results["supervised"].append({
                    "model": name,
                    "type": "regression",
                    "mse": mean_squared_error(y_test, preds)
                })

        except Exception as e:
            results["supervised"].append({
                "model": name,
                "error": str(e)
            })

    # Unsupervised models
    X_unsupervised = df.drop(columns=[target_column])

    for name, model in unsupervised_models.items():
        try:
            model.fit(X_unsupervised)
            labels = model.labels_ if hasattr(model, "labels_") else model.predict(X_unsupervised)
            score = silhouette_score(X_unsupervised, labels)

            results["unsupervised"].append({
                "model": name,
                "silhouette_score": score
            })

        except Exception as e:
            results["unsupervised"].append({
                "model": name,
                "error": str(e)
            })

    return results





# def build_models(df, target_column):
#     X = df.drop(columns=[target_column])
#     y = df[target_column]

#     # Determine if the task is classification or regression
#     if y.dtype == 'object' or y.dtype.name == 'category':
#         is_classification = True
#     elif np.issubdtype(y.dtype, np.number):
#         if len(y.unique()) <= 3:
#             is_classification = True
#         else:
#             is_classification = False
#     else:
#         is_classification = False

#     # Round and convert to integer if classification
#     if is_classification and not np.issubdtype(y.dtype, np.integer):
#         y = y.round().astype(int)

#     # Define supervised models
#     supervised_models = {
#         "Decision Tree": DecisionTreeClassifier() if is_classification else DecisionTreeRegressor(),
#         "Random Forest": RandomForestClassifier() if is_classification else RandomForestRegressor(),
#         "SVM": SVC() if is_classification else SVR(),
#         "K-Nearest Neighbors": KNeighborsClassifier() if is_classification else KNeighborsRegressor(),
#         "Naive Bayes": GaussianNB() if is_classification else None,
#     }

#     if is_classification:
#         supervised_models["Logistic Regression"] = LogisticRegression(max_iter=1000)

#     # Define unsupervised models
#     unsupervised_models = {
#         "K-Means Clustering": KMeans(n_clusters=5, random_state=42),
#         "DBSCAN": DBSCAN(eps=0.5, min_samples=5),
#         "Agglomerative Clustering": AgglomerativeClustering(n_clusters=5)
#     }

#     results = {
#         "supervised": [],
#         "unsupervised": []
#     }

#     # Supervised training
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#     for name, model in supervised_models.items():
#         if model is None:
#             results["supervised"].append(f"✘ {name} not supported for regression tasks.")
#             continue

#         try:
#             model.fit(X_train, y_train)
#             preds = model.predict(X_test)

#             if is_classification:
#                 results["supervised"].append(f"✅ {name} Accuracy: {accuracy_score(y_test, preds):.4f}")
#                 results["supervised"].append(f"Confusion Matrix:\n{confusion_matrix(y_test, preds)}")
#                 results["supervised"].append(f"Classification Report:\n{classification_report(y_test, preds)}")
#             else:
#                 results["supervised"].append(f"✅ {name} MSE (Mean Squared Error): {mean_squared_error(y_test, preds):.4f}")
#         except Exception as e:
#             results["supervised"].append(f"❌ {name} failed: {str(e)}")

#     # Unsupervised training
#     X_unsupervised = df.drop(columns=[target_column])

#     for name, model in unsupervised_models.items():
#         try:
#             model.fit(X_unsupervised)
#             cluster_labels = model.labels_
#             score = silhouette_score(X_unsupervised, cluster_labels)
#             results["unsupervised"].append(f"✅ {name} Silhouette Score: {score:.4f}")
#         except Exception as e:
#             results["unsupervised"].append(f"❌ {name} failed: {str(e)}")

#     return results