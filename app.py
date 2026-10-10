import streamlit as st

st.set_page_config(
    page_title="Góc Pha Chế",
    page_icon="🥤",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #fffaf2;
}
h1, h2, h3 {
    color: #315b45;
}
.recipe {
    background: white;
    padding: 16px;
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

st.title("🥤 GÓC PHA CHẾ")
st.subheader("Tự tay pha chế – Thỏa sức sáng tạo")
st.write(
    "Khám phá những công thức đồ uống ngon, "
    "dễ làm và phù hợp với ngân sách của bạn."
)

menu = st.columns(5)
with menu[0]:
    st.write("🏠 Trang chủ")
with menu[1]:
    st.write("☕ Cà phê")
with menu[2]:
    st.write("🍵 Trà")
with menu[3]:
    st.write("🍓 Sinh tố")
with menu[4]:
    st.write("📖 Mẹo pha chế")

recipes = [
    {
        "name": "Trà đào cam sả",
        "category": "Trà",
        "time": 10,
        "cost": 12000,
        "ingredients": [
            "150 ml trà đen đã pha",
            "20 ml siro đào",
            "2 miếng đào ngâm",
            "2 lát cam",
            "Sả và đá viên tùy thích"
        ],
        "steps": [
            "Pha trà và để nguội.",
            "Cho trà, siro đào và đá vào ly.",
            "Thêm đào, cam và sả.",
            "Khuấy đều rồi thưởng thức."
        ]
    },
    {
        "name": "Matcha latte",
        "category": "Trà sữa",
        "time": 5,
        "cost": 15000,
        "ingredients": [
            "2 g bột matcha",
            "50 ml nước ấm",
            "150 ml sữa tươi",
            "Đá viên tùy thích"
        ],
        "steps": [
            "Rây bột matcha vào cốc.",
            "Thêm nước ấm và khuấy tan.",
            "Cho đá và sữa vào ly.",
            "Rót matcha lên trên và thưởng thức."
        ]
    },
    {
        "name": "Cà phê sữa đá",
        "category": "Cà phê",
        "time": 7,
        "cost": 10000,
        "ingredients": [
            "20 g cà phê xay",
            "60 ml nước nóng",
            "25 ml sữa đặc",
            "Đá viên tùy thích"
        ],
        "steps": [
            "Cho cà phê vào phin và pha với nước nóng.",
            "Cho sữa đặc vào ly.",
            "Thêm cà phê đã pha và khuấy đều.",
            "Cho đá vào ly rồi thưởng thức."
        ]
    },
    {
        "name": "Sinh tố xoài",
        "category": "Sinh tố",
        "time": 5,
        "cost": 12000,
        "ingredients": [
            "150 g xoài chín",
            "100 ml sữa tươi",
            "Một ít sữa chua",
            "Đá viên tùy thích"
        ],
        "steps": [
            "Gọt vỏ và cắt nhỏ xoài.",
            "Cho xoài, sữa và sữa chua vào máy xay.",
            "Thêm đá nếu muốn.",
            "Xay mịn rồi rót ra ly."
        ]
    }
]

st.divider()
st.header("🔎 Khám phá công thức")

keyword = st.text_input(
    "Bạn muốn pha chế món gì?",
    placeholder="Ví dụ: matcha, trà đào, cà phê..."
)

categories = [
    "Tất cả", "Cà phê", "Trà",
    "Trà sữa", "Sinh tố"
]

category = st.selectbox(
    "Chọn danh mục",
    categories
)

filtered = [
    r for r in recipes
    if keyword.lower() in r["name"].lower()
    and (
        category == "Tất cả"
        or r["category"] == category
    )
]

st.caption(f"Có {len(filtered)} công thức phù hợp.")

for recipe in filtered:
    with st.expander(
        f"🥤 {recipe['name']} · {recipe['time']} phút"
    ):
        st.write(f"**Danh mục:** {recipe['category']}")
        st.write(f"**Thời gian:** {recipe['time']} phút")
        st.write(
            f"**Chi phí dự kiến:** "
            f"{recipe['cost']:,} đồng/ly"
        )

        st.subheader("Nguyên liệu")
        for item in recipe["ingredients"]:
            st.write(f"- {item}")

        st.subheader("Cách thực hiện")
        for i, step in enumerate(recipe["steps"], 1):
            st.write(f"**Bước {i}:** {step}")

        st.info(
            "Chi phí chỉ là ước tính, có thể thay đổi "
            "theo giá nguyên liệu tại địa phương."
        )

st.divider()
st.write(
    "© Góc Pha Chế | Chia sẻ niềm vui tự pha đồ uống"
)

