set datafile separator ','

set xdata time # tells gnuplot the x axis is time data
set xtics rotate # rotate labels on the x axis

set timefmt "%Y-%m-%dT%H:%M:%S" # specify our time string format
#set format x "%Y-%m-%d %H:%M:%S" # otherwise it will show only MM:SS
set format x "%H:%M" # otherwise it will show only MM:SS

set key autotitle columnhead # use the first line as title
set key top right outside
set ylabel "Temp (C)" # label for the Y axis
set ytics 
set xlabel 'Time' # label for the X axis
set xtics font ",5"
set title "Temp Sensors"

plot "CHA01001.csv" using 10:6 with lines ,  \
"CHA01002.csv" using 10:6 with lines ,  'co2.csv' using 1:4 with lines , 'co2.csv' using 1:5 with lines 
