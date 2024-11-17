import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['Casas', 'Apartamentos', 'Terrenos', 'Sítios']
    valores = [100, 200, 300, 400]
    
    fig, ax = plt.subplots()
    ax.pie(valores, labels=labels, autopct='%1.1f%%')
    plt.savefig('pie_chart.png')
    plt.close()

generate_pie_chart()