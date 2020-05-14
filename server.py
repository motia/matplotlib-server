import io
from flask import Flask, Response, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/<chart>/plot.png')
def plot_png(chart):
    x = [float(t) for t in request.args.get('x').split(',')]
    y = [float(t) for t in request.args.get('y').split(',')]
    xTicks = [float(t) for t in request.args.get('x_ticks').split(',')]
    yTicks = [float(t) for t in request.args.get('y_ticks').split(',')]
    xLabels = request.args.get('x_labels').split(',')
    yLabels = request.args.get('y_labels').split(',')

    fig = create_figure(x, y, xTicks, xLabels, yTicks, yLabels, chart)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure(x, y, xTicks, xLabels, yTicks, yLabels, chart):
  fig = plt.figure(figsize=(10, 8))
  ax = fig.add_subplot(111)

  if (chart == 'bar'):
    plt.bar(x, y, width=0.6)
  else:
    plt.plot(x, y)
    ax.fill_between(x, 0, y, facecolor='aqua')
    ax.autoscale(enable=True, axis='y', tight=True)
  
  ax.yaxis.tick_right()

  # Hide the left and top spines
  ax.spines['left'].set_visible(False)
  ax.spines['top'].set_visible(False)

  # Only show ticks on the left and bottom spines
  ax.yaxis.set_ticks_position('right')
  ax.xaxis.set_ticks_position('bottom')

  # setting x ticks
  ax.set_xticks(xTicks)
  ax.set_xticklabels(xLabels)

  # setting y ticks
  ax.set_yticks(yTicks)
  ax.set_yticklabels(yLabels)

  return fig

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
