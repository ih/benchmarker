commandArgs()[5]
commandArgs()[6]
inFile = commandArgs()[5]
outFile = commandArgs()[6]

runTimes = read.table(inFile,  header=TRUE, sep=" ")
boxplot(runTimes)
dev.copy(device=jpeg,file=outFile)
dev.off()
