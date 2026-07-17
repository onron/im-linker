import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 0. 페이지 기본 세팅 및 iM뱅크 테마 정의
# ==========================================
st.set_page_config(page_title="iM 로컬-링커 데모", page_icon="🏦", layout="wide")

# iM뱅크 브랜드 컬러 스타일 적용 (Sky Blue & Dark Blue)
st.markdown("""
    <style>
    .main-title {
        font-size: 32px;
        font-weight: bold;
        color: #0083B0;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 16px;
        color: #666666;
        margin-bottom: 25px;
    }
    .status-card {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0083B0;
        margin-bottom: 15px;
    }
    .metric-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 헤더 영역
st.markdown('<div class="main-title">🏦 iM 로컬-링커 (iM Local-Linker)</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">AI 기반 소상공인 상시 상권 대응 & 상생 플랫폼 | 가점 5점 실구현 데모 (팀 경로당)</div>', unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# 1. 사이드바 - 실시간 소상공인 프로필 제어
# ==========================================
st.sidebar.markdown("### 👤 소상공인 내 가게 설정")
shop_name = st.sidebar.text_input("가게 이름 입력", "경로당 치킨")
shop_type = st.sidebar.selectbox(
    "업종 분류", 
    ["외식업 (치킨·한식·카페 등)", "소모품 서비스업 (미용실 등)", "로컬 리테일 (꽃집·소품샵 등)"]
)
st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip:** 이 데모는 소상공인 사장님이 매일 아침 매장 문을 열며 확인하는 'iM 로컬-링커 가맹점주 앱'의 핵심 기능 시뮬레이션입니다.")

# 메인 화면 기능을 3가지 탭으로 분할
tab1, tab2, tab3 = st.tabs(["📊 1. AI 상시 상권 예측", "🤝 2. Agentic 공동구매", "📈 3. 매출 흐름 분석 & 대출 추천"])

# ==========================================
# Tab 1: AI 상시 상권 예측 (Daily + Peak)
# ==========================================
with tab1:
    st.markdown("### 📊 AI 상시 상권 예측 엔진 (Daily & Peak)")
    st.write("iM뱅크의 내부 오프라인 카드 결제 데이터와 지자체 제공 실시간 유동인구 API를 세만틱 레이어(Semantic Layer)로 결합하여 매장의 최적 재고 및 행동 지침 카드를 생성합니다.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("⚙️ 외부 변수 시뮬레이터")
        weather_select = st.selectbox("오늘의 날씨", ["맑음 ☀️", "우천/비 예보 🌧️"])
        event_select = st.selectbox(
            "인근 지역 축제/이벤트 상황", 
            ["평범한 일상 (이벤트 없음)", "대구 치맥 페스티벌 🍗", "지역 골목 상권 소규모 행사 🎈"]
        )
        
    with col2:
        st.subheader("💡 AI 에이전트 분석 결과 & 행동 지침")
        
        # 1단계: 날씨 및 이벤트 변수에 따른 동적 조건 처리
        if event_select == "평범한 일상 (이벤트 없음)":
            if weather_select == "우천/비 예보 🌧️":
                st.markdown(f"""
                <div class="status-card">
                    <h4>🌧️ [평시 일상 모드] 우천 대비 자재 최적화</h4>
                    <p>내일 대구 지역에 비 예보가 있어 매장 앞 오프라인 도보 유동인구는 평소 대비 <b>15% 감소</b>할 것으로 예측됩니다.</p>
                    <p>그러나 과거 iM 결제 통계상 배달 주문량이 <b>20%p 상승</b>하는 경향을 보입니다. <b>포장 및 배달용 부자재 재고를 15% 추가 확보</b>하시길 권장합니다.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="status-card">
                    <h4>☀️ [평시 일상 모드] 정상 운영 가이드</h4>
                    <p>내일은 맑은 날씨가 유지되며, 상권 내 유동인구 및 예상 매출 변동폭이 평소 수준(±3%) 이내로 매우 안정적입니다.</p>
                    <p>자재의 추가 확보 없이 <b>기존 정량 재고(Standard Inventory)</b>를 유지하셔도 좋습니다.</p>
                </div>
                """, unsafe_allow_html=True)
                
        elif event_select == "대구 치맥 페스티벌 🍗":
            st.markdown(f"""
            <div class="status-card" style="border-left: 5px solid #ff4b4b; background-color: #fff5f5;">
                <h4 style="color: #ff4b4b;">🚨 [피크 모드 자동 전환] 대구 치맥 페스티벌 대목 기간!</h4>
                <p>축제 행사장 동선 분석 결과, <b>{shop_name}</b> 매장 바로 앞 유동인구가 평시 대비 <b>180% 폭증</b>할 것으로 분석됩니다.</p>
                <p>핵심 소비 타깃은 <b>20대 남성/여성</b>이며, 예상 야간 피크 타임은 20시~23시입니다.</p>
                <p><b>⚠️ 추천 행동 지침:</b> 식자재 및 주류 재고를 평소보다 <b>최소 25% 이상 사전 추가 확보</b>하여 매출 기회 손실을 방지하십시오!</p>
            </div>
            """, unsafe_allow_html=True)
            
        elif event_select == "지역 골목 상권 소규모 행사 🎈":
            st.markdown(f"""
            <div class="status-card">
                <h4>🎈 [피크 모드 자동 전환] 인근 지역 행사 감지</h4>
                <p>인근 500m 이내 소규모 골목 축제가 예정되어 있습니다. 오전 시간대 가족 단위 유동인구가 약 35% 증가할 것으로 예상됩니다.</p>
                <p>가족 타깃용 식자재 및 매장 내 소모품 재고를 평소 대비 <b>10% 추가 준비</b>해 두는 것을 권장합니다.</p>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# Tab 2: Agentic 공동구매 클러스터링
# ==========================================
with tab2:
    st.markdown("### 🤝 Agentic 골목 공동구매 시스템 (Cluster-Based Group Purchasing)")
    st.write("나홀로 대량 자재를 사기 어려운 소상공인들을 위해, AI 에이전트가 반경 1.5km 이내의 동종 업종 사장님들의 공동구매 요청을 묶고(클러스터링), iM뱅크의 기존 B2B 대형 물류 파트너사 트럭을 통해 가게 앞까지 원스톱 무료 순회 배송을 보장합니다.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🛒 실시간 자재 발주 입력")
        # 업종에 따른 기본 추천 품목 제어
        if "외식업" in shop_type:
            default_item = "생닭 및 튀김 식재료"
            default_qty = 50
        elif "서비스업" in shop_type:
            default_item = "고급 염색약 및 샴푸 팩"
            default_qty = 30
        else:
            default_item = "선물용 플라워 박스 소모품"
            default_qty = 20
            
        purchase_item = st.text_input("공동구매가 필요한 품목", default_item)
        purchase_qty = st.number_input("필요 수량 입력", min_value=10, value=default_qty, step=10)
        
        # 공동구매 발주 버튼
        run_purchase = st.button("공동구매 수요 매칭 매커니즘 실행 🚀")
        
    with col2:
        st.subheader("🔄 iM 로컬-링커 AI 알고리즘 연산")
        if run_purchase:
            st.success(f"✔️ {shop_name} 사장님의 '{purchase_item}' 주문이 접수되었습니다. AI가 반경 1.5km 이내 동종 상권 매칭 중...")
            
            # 시뮬레이션 매칭 결과 테이블 출력
            simulated_matches = {
                "가맹점명": [shop_name, "수성 골목 상회", "범어 로컬 빌리지", "하안 로컬 스토어"],
                "신청 수량": [purchase_qty, int(purchase_qty * 1.2), int(purchase_qty * 0.8), int(purchase_qty * 1.5)],
                "매칭 결과": ["내 가맹점", "AI 자동 매칭 완료 ✔️", "AI 자동 매칭 완료 ✔️", "AI 자동 매칭 완료 ✔️"]
            }
            df_match = pd.DataFrame(simulated_matches)
            st.table(df_match)
            
            total_sum = sum(simulated_matches["신청 수량"])
            
            # 매칭 규모에 따른 유동적 할인률 및 물류 혜택 계산
            discount = 18 if total_sum >= 100 else 10
            
            m1, m2, m3 = st.columns(3)
            with m1:
                st.markdown(f'<div class="metric-box"><h5>총 취합 물량</h5><h3>{total_sum} 개</h3></div>', unsafe_allow_html=True)
            with m2:
                st.markdown(f'<div class="metric-box"><h5 style="color:#ff4b4b;">유통사 협상 할인율</h5><h3 style="color:#ff4b4b;">{discount}% 절감</h3></div>', unsafe_allow_html=True)
            with m3:
                st.markdown(f'<div class="metric-box"><h5>물류 방식</h5><h6 style="color:#0083B0;">대구 B2B 정기루트 무료배송</h6></div>', unsafe_allow_html=True)
                
            st.markdown("""
            ---
            **📦 [B2B 물류 파트너망 순회 배송 연동]**
            * 본 공동구매가 마감되면, iM뱅크의 대형 기업 고객인 **'대구경북 종합자재도매종합물류'**의 정기 배송 노선 차량에 해당 물량이 자동으로 적재되어 각 매장 앞으로 정시 새벽 배송됩니다. 
            * **이를 통해 물류 비용 제로화 및 원재료 매입원가 평균 18%를 즉시 절감합니다.**
            """)
        else:
            st.info("왼쪽에서 필요한 자재 품목과 수량을 입력하고 버튼을 눌러 공동구매 클러스터링 알고리즘을 테스트해보세요.")

# ==========================================
# Tab 3: 매출 흐름 분석 & 대출 추천
# ==========================================
with tab3:
    st.markdown("### 📈 매출 흐름 분석 및 상생 자산 관리 (Moody's AI Framework)")
    st.write("소상공인의 최근 6개월 매출 궤적을 바탕으로 가맹점의 재정 건강 상태를 실시간 진단하고, 대목(축제) 직전 단기 원자재 매입 자금이 긴급하게 필요할 때 행원 대면 없이 맞춤형 금융 상품을 추천해 드립니다.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📈 최근 6개월 매출 흐름 Trend (iM 가맹점 결제 데이터 연동)")
        
        # 가상의 6개월 매출 변동 데이터 플로팅
        months = ["2월", "3월", "4월", "5월", "6월", "7월(예상)"]
        rev_data = [1250, 1300, 1150, 1400, 980, 1950] # 6월이 바닥, 7월 대목에 폭증하는 시나리오
        
        fig, ax = plt.subplots(figsize=(10, 4.5))
        ax.plot(months, rev_data, marker='o', color='#0083B0', linewidth=3, label="월 매출 추이")
        ax.fill_between(months, rev_data, color='#0083B0', alpha=0.1)
        ax.axhline(y=1000, color='r', linestyle='--', alpha=0.5, label="고정 원가 임계점")
        
        ax.set_ylabel("매출 (단위: 만 원)", fontsize=10)
        ax.set_title(f"{shop_name} 매장 최근 결제 금액 흐름 분석", fontsize=12, fontweight='bold')
        ax.legend(loc="upper left")
        ax.grid(True, linestyle=':', alpha=0.6)
        
        st.pyplot(fig)
        
    with col2:
        st.subheader("🔍 AI 매장 금융 진단 보고서")
        
        st.error("⚠️ **6월 일시적 현금 유동성 경고**")
        st.markdown(f"""
            * 6월 상권 정체로 일시적 매출 하락 발생(980만 원) ➔ 임계값 이하로 현금 흐름 경색 상태.
            * **반전 요인:** 7월 대구 치맥페스티벌 기간 중 **{shop_name}**의 예상 매출은 **1,950만 원**으로 분석되어 유동성 급반등이 확실시됩니다.
        """)
        
        st.markdown("---")
        st.subheader("🏦 맞춤형 대출 추천")
        st.markdown("""
            **[iM 미래매출 연계 상생 신용대출]**
            * **상품 한도:** **최대 1,500만 원** (7월 피크 대목 예상 미래매출액 담보 가산 적용)
            * **실행 금리:** **연 3.9%** (ESG 골목상권 공동구매 참여 가점 적용)
            * **상환 조건:** 대목 기간 매출 정산 시 일일 매출에서 안전 자동 공제 상환 옵션 제공
        """)
        
        loan_btn = st.button("내 한도 확인 및 대출 신청 💳")
        if loan_btn:
            st.balloons()
            st.success("🎉 대출 사전 심사 신청이 성공적으로 접수되었습니다! iM뱅크의 리스크 관리 심사 모델을 통해 3초 이내에 최종 확정 한도가 고지됩니다.")