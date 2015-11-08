require(ggplot2)
pdf(file='jeopardy.pdf', height=8.5, width=11, onefile=TRUE, pointsize=12)

jpty <- read.table('data.csv', sep=",", header=TRUE)
aggdata <-aggregate(jpty, by=list(year = jpty$year), FUN=mean)

g <- ggplot(data = aggdata, aes(x = year, y = reading))
#g + geom_point(aes(color = year)) +  geom_smooth(method = "lm", se=FALSE, color="black", aes(group=2))

#title(main="Reading Level of Jeopardy! Games over Time", sub="with data from J! Archive", xlab="year episode aired", ylab="Automated Readibility Index value")

#g + geom_point(aes(color = year)) + geom_smooth(aes(group=1), method="lm", fullrange=TRUE)

g + geom_line() + ggtitle("Reading Level of Jeopardy! Games over Time") +
  labs(x="year episode aired",y="Automated Readibility Index value") 
