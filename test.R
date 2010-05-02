
## list the arguments passed into the program.
commandArgs()

## Now to parse the command line options
## If there is an = sign in the arg then it is parsed and the
## first part of the arg is treated as the variable name with
## the second being the value of the argument.
## If there is no = sign then the arg value is assigned TRUE
##
## Note that we do character it integer conversion for variables whose name ends
## with an I (integer) and N (floating/integer). This is done of course because
## the command Line arguments come in as strings.

for (e in commandArgs()) {
  ta = strsplit(e,"=",fixed=TRUE)
  if(! is.na(ta[[1]][2])) {
    temp = ta[[1]][2]
    if(substr(ta[[1]][1],nchar(ta[[1]][1]),nchar(ta[[1]][1])) == "I") {
      temp = as.integer(temp)
    }
    if(substr(ta[[1]][1],nchar(ta[[1]][1]),nchar(ta[[1]][1])) == "N") {
      temp = as.numeric(temp)
    }
    assign(ta[[1]][1],temp)
    cat("assigned ",ta[[1]][1]," the value of |",temp,"|\n")
  } else {
    assign(ta[[1]][1],TRUE)
    cat("assigned ",ta[[1]][1]," the value of TRUE\n")
  }
}




## generate the name we will use for the vector
name = paste("normal",numI,meanN,stdN,sep="_",collapse="")

## generate the random normals
assign(name,rnorm(numI,meanN,stdN))

## generate the name we will use for the data file
file = paste(numI,meanN,stdN,"normal",sep="-",collapse="")
file = paste(file,"RData",sep=".",collapse="")
file

## save the data
 save.image(file="hello",ascii=TRUE)
