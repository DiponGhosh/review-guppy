import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import StringIO

def PieResult(sizes):
    labels = ['positive', 'negative', 'neutral']
    colors = ['#2E7D32', '#D32F2F', '#F57C00']

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
    img = StringIO()
    img_src = './static/images/pie/' + str(img) + '.png'
    plt.savefig(img_src)
    return img_src

#list_reult = ['75.00', '5.00', '20.00']
#PieResult(list_reult)