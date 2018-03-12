import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def PieResult(sizes):
    labels = ['positive', 'neutral', 'negative']
    colors = ['#2E7D32', '#F57C00', '#D32F2F']

    plt.title('Review Analysis')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=False, startangle=90)


    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.tight_layout()
    #plt.show()
    plt.savefig('./static/images/result_pie.png')

#list_reult = ['75.00', '5.00', '20.00']
#PieResult(list_reult)