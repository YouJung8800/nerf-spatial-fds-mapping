import pandas as pd
import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, FunctionTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

# 1. 정교화된 물리 기반 공간 특징 추출기
def spatial_physical_processor(data):
    results = []
    for points in data:
        if not isinstance(points, list) or len(points) == 0:
            results.append([0.0, 0.0])
            continue
        density = len(points)
        stability = 1.0 / (np.std(points) + 0.1) if np.std(points) > 0 else 1.0
        results.append([float(density), float(stability)])
    return np.array(results)

class SpatialFinTechEngine:
    def __init__(self):
        # 파이프라인 구축
        preprocessor = ColumnTransformer([
            ('financial', StandardScaler(), ['monthly_sales', 'return_rate', 'settlement_days']),
            ('contextual', TfidfVectorizer(max_features=50), 'review_summary'),
            ('spatial_physics', FunctionTransformer(spatial_physical_processor), 'warehouse_3d_points')
        ])
        self.model = Pipeline([
            ('preprocessor', preprocessor), 
            ('classifier', HistGradientBoostingClassifier(random_state=42))
        ])

    def train(self, df):
        X = df[['monthly_sales', 'return_rate', 'settlement_days', 'review_summary', 'warehouse_3d_points']]
        self.model.fit(X, df['is_default'])
        print("✓ [시스템 로그] Spatial-FinTech 정교화 엔진 학습 완료")

    def predict_and_explain(self, data):
        prob = self.model.predict_proba(data)[0][1]
        score = int(1000 - (prob * 700))
        return score, "물리적 적재 밀도 및 재무 건전성 분석 결과 반영됨"

def main():
    data = pd.DataFrame({
        'monthly_sales': [500.0, 1500.0, 200.0, 900.0],
        'return_rate': [5.0, 1.0, 25.0, 4.0],
        'settlement_days': [1, 3, 15, 2],
        'review_summary': ["보통", "최상", "최악", "좋음"],
        'warehouse_3d_points': [[1,2], [1,2,3,4,5], [1], [1,2,3,4]],
        'is_default': [0, 0, 1, 0]
    })
    
    engine = SpatialFinTechEngine()
    engine.train(data)
    
    new_data = pd.DataFrame({
        'monthly_sales': [1100.0], 'return_rate': [2.5], 'settlement_days': [2], 
        'review_summary': ["배송 빠름"], 'warehouse_3d_points': [[1,2,3,4]]
    })
    
    score, explain = engine.predict_and_explain(new_data)
    print(f"\n[최종 심사 결과: {score}점]")
    print(f"상세 근거: {explain}")

if __name__ == "__main__":
    main()
