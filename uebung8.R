#1

X = c(10,11,12,14,15,16)
Y = c(22,19,20,21,15,17)
df = data.frame(X,Y)

#   X  Y
#1 10 22
#2 11 19
#3 12 20
#4 14 21
#5 15 15
#6 16 17

plot(X,Y,xlab="x",ylab="y",xlim=c(0,25),ylim=c(0,25))

#2

mean(X)
#[1] 13
mean(Y)
#[1] 19

#3

Reg <- lm(Y~X)
Reg

#Call:
#lm(formula = Y ~ X)

#Coefficients:
#(Intercept)            X  
#    29.2143      -0.7857  

# Also r(x)=29.2143-0.7857x

#4

abline(Reg)

#5

cor(X,Y)
#[1] -0.7130241

#Der Korrrelationskoeffizient zeigt an ob zwischen Werten ein linearer Zusammenhang besteht. Im Beispiel besteht also ein negativer linearer Zusammenhang, es fällt also Y wenn X steigt.




