import pandas as pd
import os
import matplotlib.pyplot as plt


def load_data(path):
   
    print("Veriler okunuyor...")
    files = [file for file in os.listdir(path) if file.endswith('.csv')]
    
    all_months_data = pd.DataFrame()
    
    for file in files:
        file_path = os.path.join(path, file)
        current_data = pd.read_csv(file_path)
        all_months_data = pd.concat([all_months_data, current_data])
        
    print(f"Başarılı! Toplam {len(files)} dosya birleştirildi.")
    return all_months_data


def clean_data(df):
    
    print("Veri temizleniyor ve işleniyor...")
    
   
    df = df.dropna(how='all')
    df = df[df['Order Date'] != 'Order Date']
    
    
    df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'])
    df['Price Each'] = pd.to_numeric(df['Price Each'])
    
    
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%y %H:%M')
    
    
    df['Sales'] = df['Quantity Ordered'] * df['Price Each']
    df['Month'] = df['Order Date'].dt.month
    
    
    def get_city(address):
        return address.split(',')[1]
    
    df['City'] = df['Purchase Address'].apply(lambda x: get_city(x))
    
    print("Temizlik tamamlandı!")
    return df


def analyze_data(df):
    
    print("Grafikler çiziliyor...")
    
    
    results = df.groupby('Month').sum(numeric_only=True)
    months = range(1, 13)
    
    plt.figure(figsize=(10, 6))
    plt.bar(months, results['Sales'])
    plt.xticks(months)
    plt.ylabel('Sales in USD ($)')
    plt.xlabel('Month number')
    plt.title('Monthly Sales Analysis')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show() 
    

if __name__ == "__main__":
    
    
    data_path = './SalesData'
    
    
    ham_veri = load_data(data_path)
    temiz_veri = clean_data(ham_veri)
    
    
    print("\n--- İlk 5 Satır ---")
    print(temiz_veri.head())
    
    
    analyze_data(temiz_veri)