# 🌱 Soil Classification Report Generator

A multilingual Streamlit application for automated soil data classification and professional PDF report generation.

## 🌐 Languages

- 🇧🇷 **Portuguese** (Português) - Default
- 🇺🇸 **English** - Full translation available

## 🚀 Quick Start

### Online Demo
Visit our [Streamlit Cloud deployment](https://your-app-url.streamlit.app) to try the app without installation.

### Local Installation
```bash
pip install -r requirements_streamlit_cloud.txt
streamlit run streamlit_soil_report.py
```

## 📊 Features

### 🔬 Advanced Analysis
- **Automatic Classification**: MB→MBom and B→MAlto systems
- **Statistical Analysis**: Mean, std deviation, median by treatment groups
- **Interactive Visualizations**: Box plots, histograms, comparisons
- **Multi-column Grouping**: Analyze by treatment, time, depth, etc.

### 📈 Visualizations
- Classification summary charts
- Parameter-specific distributions
- Treatment comparison charts
- Box plots for group analysis

### 📄 Reports
- **Professional PDF Reports**: Automated generation
- **Excel Export**: Classified data + statistics
- **CSV Downloads**: Individual parameter statistics

### 🛠️ Customization
- Add custom parameters
- Flexible column mapping
- Multiple grouping options

## 📋 Data Format

Your file should contain at least these columns:

| Parameter | Numerical Result | Treatment | Time | Depth |
|-----------|------------------|-----------|------|-------|
| pH in CaCl2 | 5.5 | control | PRE_APPLICATION | 0.1 |
| Organic Matter | 25.3 | NPK | POST_APPLICATION | 0.3 |
| Calcium | 3.2 | control | PRE_APPLICATION | 0.1 |

### Required Columns
- **Parameter**: Soil parameter names
- **Numerical Result**: Values for classification

### Optional Columns
- **Treatment** (Tratamento): Control vs treatments
- **Time** (Tempo): Sampling period
- **Depth**: Sample depth in meters
- **Units**: Measurement units

## 🎯 Supported Parameters

### Macronutrients (MB→MBom Scale)
- Organic Matter (Matéria orgânica)
- Calcium (Cálcio trocável)
- Magnesium (Magnésio trocável)
- Potassium (Potássio trocável)
- Available Phosphorus (P disponível)

### pH & Saturation (B→MAlto Scale)
- pH in CaCl₂
- pH in H₂O
- Base Saturation (Saturação por bases)
- Aluminum Saturation (Saturação por alumínio)*

### CTC & Acidity
- Effective CTC (CTC efetiva)
- CTC at pH 7.0 (CTC a pH 7,0)
- Exchangeable Acidity (Acidez trocável)*
- Potential Acidity (Acidez potencial)*

### Micronutrients
- Copper, Iron, Manganese, Zinc, Sulfur

*_Inverted scale: lower values are better_

## 🎨 Classification Colors

- 🔴 **Very Low/Low**: Red/Orange
- 🟡 **Medium**: Yellow
- 🟢 **Good/High**: Green shades

## 🚀 Deployment

### Streamlit Cloud
1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set main file: `streamlit_soil_report.py`
5. Deploy!

### Local Development
```bash
git clone your-repo-url
cd soil-classification-app
pip install -r requirements_streamlit_cloud.txt
streamlit run streamlit_soil_report.py
```

## 📁 Files for Deployment

### Essential Files
- `streamlit_soil_report.py` - Main application
- `requirements_streamlit_cloud.txt` - Dependencies

### Documentation
- `README.md` - This file (English)
- `README_Streamlit_App_EN.md` - Detailed English docs
- `README_Streamlit_App.md` - Portuguese documentation
- `INSTALL_GUIDE_EN.md` - Installation troubleshooting

## 🌟 Example Usage

1. **Upload** your soil data (Excel/CSV)
2. **Select language** (Portuguese/English)
3. **Map columns** (Parameter, Values)
4. **Run classification**
5. **Analyze results** by treatment groups
6. **Generate reports** (PDF/Excel)

## 🧪 Statistical Analysis

### Group Comparisons
- Compare treatments (control vs NPK)
- Analyze by sampling time
- Multi-factor analysis (treatment + time)

### Visualizations
- Box plots showing distribution differences
- Histograms grouped by treatments
- Statistical comparison charts

### Export Options
- Individual parameter statistics (CSV)
- Complete analysis (Excel)
- Professional reports (PDF)

## 🐛 Troubleshooting

See `INSTALL_GUIDE_EN.md` for detailed installation help.

Common issues:
- **Python version**: Requires 3.7+
- **Missing packages**: Use `requirements_streamlit_cloud.txt`
- **Data format**: Ensure column names match expected format

---

**Developed to facilitate soil data analysis and classification** 🌱

*Supporting sustainable agriculture through data-driven insights*
