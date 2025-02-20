# IBM_Main_Project
Main Project For Internship By VTU - Customer Journey Analysis Using Clustering and Dimensionality Reduction


##  Overview  
This project performs customer segmentation using clustering techniques to analyze wholesale customer data. The goal is to identify distinct customer groups based on purchasing behavior.  

##  Dataset  
The dataset used is **Wholesale customers data.csv**, which contains customer purchase details categorized by region and channel.  

##  Technologies Used  
- Python  
- Pandas & NumPy (Data Manipulation)  
- Matplotlib & Seaborn (Data Visualization)  
- Scikit-Learn (Clustering, PCA)  
- SciPy & StatsModels (Statistical Analysis)  

## 🔄 Workflow  
### 1. Data Preprocessing  
- Checked for missing values and data types  
- Mapped categorical values (Region & Channel)  
- Applied Box-Cox transformation for normalization  
- Scaled numerical data using MinMaxScaler  
- Removed outliers using IQR  

### 2. Clustering Models  
- **K-Means Clustering**  
  - Used the Elbow Method to determine the optimal number of clusters  
  - Applied PCA for dimensionality reduction  
  - Visualized clusters in 2D  

- **Hierarchical Clustering**  
  - Applied Agglomerative Clustering with Ward’s linkage  
  - Visualized clusters using dendrograms  

### 3. Cluster Analysis  
- Compared the cluster distributions and mean values  
- Identified key differences between customer groups  

##  Results  
- Identified **3 customer segments** using K-Means clustering  
- Visualized clusters using PCA (Principal Component Analysis)  
- Compared clustering performance using hierarchical clustering  

## 🚀 How to Run  
1. Install dependencies:  
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn statsmodels
   ```  
2. Run the Python script:  
   ```bash
   python ibm_maincode.py
   ```  

## 📌 Key Findings  
- Different customer segments show varying spending behaviors across product categories.  
- PCA helps in reducing dimensions while maintaining data variance.  
- Hierarchical clustering provides an alternative view of customer grouping.  

 
