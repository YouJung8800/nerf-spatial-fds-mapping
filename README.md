# 🌐 NeRF 3D Spatial Mapping & Occlusion Analysis Engine for Financial Risk Detection

> **본 프로젝트는 3D 공간 지형지물 스캔 알고리즘을 활용하여, 금융 거래 데이터 내의 사각지대(Blind Spot) 및 이상 징후 패턴을 다차원적으로 탐지하고 시각화하는 자동화 파이프라인 솔루션의 프로토타입입니다.**

## 📌 Project Overview
기존의 2차원적인 금융 이상거래탐지(FDS) 시스템은 텍스트나 통계적 수치에만 의존하여 다층적인 금융 범죄 패턴(예: 교차 자금세탁, 역외 카드 불법 거래 밀집도)을 직관적으로 포착하기 어려웠습니다. 

본 파이프라인은 고밀도 3D 포인트 클라우드 좌표계 시뮬레이션을 통해 가시성 지수(Visibility Index)와 구조적 차단율(Occlusion Index)을 계산하며, **차단율 80% 이상의 밀폐 영역을 '사각지대(BLIND_SPOT)'로 상시 정의하여 리스크를 시각적으로 입증(Prove)**합니다. 이 구조는 추후 **카드사 실사 리스크 관리 및 불법 거래 방지 데이터**의 범용적 기술 인프라로 확장될 예정입니다.

## 🛠️ System Architecture & Pipeline
본 시스템은 데이터가 소실되거나 터미널이 닫히는 오프라인 환경을 대비하여 모든 원천 데이터와 시각화 그래픽을 디스크에 영구 백업하도록 설계되었습니다.

1. **Pipeline Infrastructure Initialization:** 공간 데이터 영구 보존을 위한 디렉토리 자동 빌드 (`./nerf_backup_workspace`)
2. **Vision Processing Scheduler:** `Nerfstudio` CLI 자동 제어 인터페이스 설계 (`ns-process-data`, `ns-train nerfacto`)
3. **High-Density Spatial Modeling:** 8,000개의 고밀도 공간 좌표계(x, y, z) 및 가시성/폐쇄도 수학적 연산 및 데이터프레임 구조화
4. **Interactive 3D Rendering & Export:** 마스킹 기법을 적용한 3D 시각화 레이어 빌드 및 고해상도 그래픽 데이터(`final_3d_render_map.png`), 공간 분석 명세서(`spatial_analysis_report.csv`) 백업

## 📊 Core Dataset Structure (`spatial_analysis_report.csv`)
생성된 공간 분석 데이터프레임은 다음과 같은 핵심 변수를 기반으로 금융 리스크의 사각지대를 정밀 평가합니다.

| Column Name | Description | Financial Interpretation (금융적 해석) |
| :--- | :--- | :--- |
| `point_id` | 공간 좌표 고유 식별자 | 특정 거래 세션 또는 가맹점 ID로 치환 가능 |
| `x`, `y`, `z` | 3차원 물리 공간 좌표 및 고도 | 거래 발생지의 지리적 위치 및 시간 축 레이어 변환 가능 |
| `visibility_index` | 공간 정밀 분석 가시성 지수 | 거래 패턴의 투명성 및 정상 거래 흐름 신뢰도 |
| `occlusion_index` | 구조적 폐쇄도 산출 지수 | **이상 거래 은닉 가능성 및 모니터링 우회 위험도** |
| `spatial_property` | `OPEN_SPACE` / `BLIND_SPOT` | **집중 관리 및 정밀 실사가 필요한 리스크 타겟팅 플래그** |

## 📈 Visualized Result
* **Open Environment Path (Blue Layer):** 정상적인 흐름을 보이는 가시 영역 데이터 파트 (투명도 조정을 통한 노이즈 최소화)
* **Structural Occlusion / Blind Spot (Red Layer):** 리스크 관리가 시급한 사각지대를 강렬한 레드 톤으로 매핑하여 의사결정권자의 인지 속도 최적화

---

## 💻 How to Run

### 1. Prerequisites
의존성 패키지를 설치합니다:
```bash
pip install numpy pandas matplotlib
