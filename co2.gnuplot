set datafile separator ','

set xdata time # tells gnuplot the x axis is time data
set xtics rotate # rotate labels on the x axis

set timefmt "%Y-%m-%dT%H:%M:%S" # specify our time string format
#set format x "%Y-%m-%d %H:%M:%S" # otherwise it will show only MM:SS
set format x "%H:%M" # otherwise it will show only MM:SS

set key autotitle columnhead # use the first line as title
set ylabel "CO2" # label for the Y axis
set y2label "temp" # label for the Y axis
set y2tics
set yrange [0:2000]
set y2range [0:100]
set xlabel 'Time' # label for the X axis
set xtics font ",5"

plot "co2.csv" using 1:2 with lines, '' using 1:3 with lines axis x1y1, '' using 1:4 with lines axis x1y2, '' using 1:5 with lines axis x1y2
#pdffigure("co2.pdf")
