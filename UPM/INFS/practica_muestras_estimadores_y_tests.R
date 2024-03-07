#############################################################################
# ESTE FICHERO ILUSTRA COMANDOS DE R PARA GENERAR MUESTRAS, REPRESENTARLAS, #
# CONSTRUIR ESTIMADORES DE PARÁMETROS E INTERVALOS ESTADÍSTICOS,            #  
# Y REALIZAR TESTS DE HIPÓTESIS                                             #
#############################################################################

# Para "limpiar" todas las variables del entorno
rm(list=ls())

# Trabajamos con 6 decimales
options(digits = 6)

#########################################################################################
# 1) GENERACION Y REPRESENTACIÓN DE MUESTRAS SINTÉTICAS A PARTIR DE UNA DISTRIBUCIÓN DADA
#########################################################################################

# La aleatoriedad de las muestras se basa en una semilla pseudo-aleatoria que
# el ordenador crea (a partir del reloj, etc.)
# Cada vez que llamamos a un comando para generar una muestra, elige una nueva semilla.

############# Generar muestras de v.a. discretas ######################

# Generar 10 tiradas segun Bernoulli con p=0.5 
#----------------------------------------------
# (Es como tener una bolsa con dos bolas -con los números 0 y 1- y 
#  sacar diez veces una bola con reemplazamiento)
sample(0:1,10,replace=T)

# Echar 10 dados (uniforme)
#---------------------------
sample(1:6,10,replace=T)

# Generar una muestra de la loteria primitiva
#--------------------------------------------
# (Es como tener una bolsa con 49 bolas numeradas de 1 a 49 y 
#  sacar 6 bolas sin reemplazamiento)
sample(1:49,6,replace=F)

# Generar muestra de tamaño 5 de binomial tamaño 10 y p=0.2
#----------------------------------------------------------
rbinom(5,10,0.2)

# Generar muestra de tamaño 10 de Poisson con lambda=3 
#-----------------------------------------------------
rpois(10, lambda = 3)

# Generar una muestra de tamaño 100 de una multinomial con cuatro posibles resultados
# que tienen unas probabilidades dadas
#----------------------------------------------
datos_multinomial <- sample(1:4,100,rep=TRUE,prob=c(.2,.3,.2,.3))
table(datos_multinomial)

######## Generar muestras de v.as. continuas ######################

# Generar muestra de uniforme 
#----------------------------
# Genero una muestra de uniforme [0,1]
runif(1)
# Muestra de tamaño 10 de uniforme [3,4]
runif(10,3,4)

#Generar muestra de normal
#-------------------------
# Muestra de tamaño 10 de normal, media 0 y desviacion estandar 1
rnorm(10)
# Muestra de tamaño 10 de normal, media 3 y desviacion estandar 1
rnorm(10,mean=3)
# Muestra de tamaño 10 de normal, media 3 y desviacion estandar 3
rnorm(10,mean=3,sd=3)

#######################  Muestras y dibujos #######################
# GENERAMOS MUESTRAS Y LAS REPRESENTAMOS

# Muestra de tamaño 100 de uniforme [1,17]
#----------------------------------------
muestra_uniforme<-runif(100,1,17)
muestra_uniforme

# Muestra de tamaño 100 de normal, media 2 y desviacion estandar 5
#-----------------------------------------------------------------
muestra_normal<-rnorm(100,2,5)
muestra_normal


# Diagramas de tallos-y-hojas y Boxplots
#---------------------------------------

# Diagrama de tallos-y-hojas y boxplot de muestra uniforme
stem(muestra_uniforme)
boxplot(muestra_uniforme)

# Diagrama de tallos-y-hojas y boxplot de muestra normal
stem(muestra_normal)
boxplot(muestra_normal)


# Histograma de muestra uniforme
#--------------------------------
puntos_corte_uniforme<-seq(1,17,0.25) 
puntos_corte_uniforme
hist(muestra_uniforme,breaks=puntos_corte_uniforme)


# Histograma y otras representaciones de muestra normal
#------------------------------------------------------
puntos_corte_normal<-seq(floor(min(muestra_normal))-1,floor(max(muestra_normal))+1,1) 
puntos_corte_normal
hist(muestra_normal,breaks=puntos_corte_normal)


# Dibujo de la "densidad empirica" (curva ajustada a los datos)
#--------------------------------------------------------------
d <- density(muestra_normal)
# Resumen derivado de los datos
d
plot(d)

plot(density(rnorm(10000)))

# Funcion de distribucion acumulativa "empirica"
#----------------------------------------------
x <- rnorm(10000)
plot(ecdf(x))


########## Tests sobre muestras #####################

# Muestra uniforme
# Probability plot (por defecto, está pensado para comparar con percentiles de una normal)
qqnorm(muestra_uniforme)
qqline(muestra_uniforme)

# Test de normalidad muestra uniforme
# Los detalles de este test no se han visto en clase pero podemos aplicarlo e interpretar
# el p-valor: la hipótesis nula, H0 es que la muestra proviene de una v.a. normal
shapiro.test(muestra_uniforme)


# Muestra normal
# Probability plot
qqnorm(muestra_normal)
qqline(muestra_normal)

# Test de normalidad
shapiro.test(muestra_normal)



#########################################################################################

###########################
# 2) ESTIMACIÓN PARAMÉTRICA
###########################

# Ejemplo de cómo influye el tamaño muestral en la calidad de los estimadores
#----------------------------------------------------------------------------
# Generamos una poblacion de N individuos con altura media mu y desviacion sigma
N <- 100000
mu <- 1.70
sigma <- 0.1

alturas <- rnorm(N,mu,sigma)

# TODA la población se puede interpretar como una como v.a. discreta que puede tomar
# tantos valores como valores distintos haya en la población, y cuya probabilidad es 
# al número de individuos con ese valor.
# Calculamos la media de TODA la poblacion (la esperanza de v.a.)
sum(alturas)/N
mean(alturas)

# Calculamos la varianza de TODA la poblacion 
sum(alturas^2)/N-mean(alturas)^2

# Nota: el comando "var" proporciona S^2, interpretando que los datos son una muestra 
# de una v.a y no una población total. Proporciona el estimador de la varianza de v.a. 
# de la que se supone hemos obtenido la muestra. 
var(alturas)
# Se puede ver la relación con la varianza de toda la población obtenida antes
var(alturas)*(N-1)/N


# Dos personas toman una muestra de la poblacion (de tamaño n_v y n_t) respectivamente
# Para un muestreo vago su tamaño muestral es n_v
n_v <- 5
muestra_vago <- sample(alturas,n_v)
muestra_vago
mean(muestra_vago)

# Para un muestreo trabajador su tamano muestral es n_t
n_t <- 100
muestra_trabajador <- sample(alturas,n_t)
muestra_trabajador
mean(muestra_trabajador)

# Experimento: cada uno de los muestreos (vago y trabajador) 
# me da un valor medio cada dia del año
medias_vago <- vector()
medias_trabajador <- vector()
for (i in (1:365))
  {
  muestra_vago <- sample(alturas,n_v)
  medias_vago[i] <- mean(muestra_vago)
  muestra_trabajador <- sample(alturas,n_t)
  medias_trabajador[i] <- mean(muestra_trabajador)
  }

# Pintamos los histogramas de las medias
# Calculo puntos de corte asociados a medias_vago y lo dejo fijo en ambos histogramas
puntos_corte<-seq((floor(100*min(medias_vago))-1)/100,(floor(100*max(medias_vago))+1)/100,by=0.01)
par(mfrow=c(1,2))
hist(medias_vago,breaks=puntos_corte,col='red')
hist(medias_trabajador,breaks=puntos_corte,col='blue')
par(mfrow=c(1,1))


# Ejemplo basado en Ejercicio 1 de hojas
#---------------------------------------
# El comando rgeom genera muestras con valor 0,1,2,... según p(x) = p (1-p)^x
# es decir es similar a la distribución geométrica pero da como resultado
# el número de tiradas (hasta obtener la primera cara) menos 1.

# Generamos aleatoriamente un valor para el parámetro p con una distribución "parecida"
# (regulable con un parámetro de variabilidad "delta") a la distribución a priori propuesta 
# para la estimación bayesiana 
# Si la variabilidad delta es 0 se corresponde exactamente con la a priori del Ejercicio 1
delta <-0.05
aux <- rbinom(1,1,3/7)
p <- aux*runif(1,min=1/3-delta,max=1/3+delta)+(1-aux)*runif(1,min=1/2-delta,max=1/2+delta)

# Tomamos una muestra de tamaño n de v.a. geométrica de probabilidad=p
# Para generar la variable vista en el ejemplo de los ejercicios, añadimos 1 a rgeom
n <- 40
muestra_geometrica <- 1+rgeom(n, p)

# Si quieres comprobar el ejemplo resuelto en clase (dos tiradas y muestra {3,2})
# puedes descomentar las dos siguiente lineas
# n < 2
# muestra_geometrica <- c(3,2)

# Estimador método de los momentos y máxima verosimilitud
p_hat_MM_ML <- n/sum(muestra_geometrica)
print(p_hat_MM_ML)

# Estimador basado en método bayesiano con 
# Distribución a priori
p1 <- 1/3
prob_priori_p1 <- 3/7
p2 <- 1/2
prob_priori_p2 <- 4/7

# Calculamos la probabilidad a posteriori 
prob_muestra <- (1-p1)^{sum(muestra_geometrica)-n}*p1^n*prob_priori_p1+(1-p2)^{sum(muestra_geometrica)-n}*p2^n*prob_priori_p2
prob_post_1 <- (1-p1)^{sum(muestra_geometrica)-n}*p1^n*prob_priori_p1/prob_muestra
prob_post_2 <- (1-p2)^{sum(muestra_geometrica)-n}*p2^n*prob_priori_p2/prob_muestra

# Elegimos p1 si prob_post_1 > prob_post_2 y viceversa
if (prob_post_1 > prob_post_2)  {p_hat_bayes <- p1} else {p_hat_bayes <- p2}
print(p_hat_bayes)

# Descubrimos el verdadero valor de p
print(p)


# Ejemplo de transparencias: estimar valor límite superior a de una v.a. uniforme [0,a] 
#---------------------------------------------------------------------------------------
# Generamos a como muestra de una uniforme [1,10]
a <- runif(1,0,10)

# Ahora generamos una muestra de la v.a. [0,a]
n <- 5
muestra <- runif(n,0,a)

# Estimadores de a
# Metodo de los momentos
a_hat_MM<- 2*mean(muestra)

# Método de ML
a_hat_ML <- max(muestra)

# MAP Bayes (mismo que ML porque la distribución a priori de a es uniforme)
a_hat_MAP <- max(muestra)


#########################################################################################

#############################
# 3) INTERVALOS DE CONFIANZA
#############################

# Ejercicio 3 de hojas. Medimos n sensores y de ellos m son defectuosos
#----------------------------------------------------------------------
# Muestra
#Total
n <- 200
# Defectuosos
m <- 8

# Construir intervalo de confianza de la proporción de defectuosos
# Estimamos la proporción
p_hat <- m/n

# Intervalo (para muestra n>>40) y para un nivel de confianza alpha
alpha <- 1-0.95
intervalo_standard <- qnorm(c(alpha/2, 1-alpha/2))
intervalo <- p_hat + sqrt(p_hat*(1-p_hat)/n)*intervalo_standard
print(intervalo)



# Ejercicio 4 de hojas. Nos proporcionan una muestras de tensión arterial de un paciente 
#---------------------------------------------------------------------------------------
# Supuestamente proviene de una variable Gaussiana de media y varianza desconocidas
muestra_tension <- c(14.5,15,16,15.5)

# Calculamos los estadísticos muestrales
x_bar <- mean(muestra_tension)
s <- sd(muestra_tension)

# Para construir el intervalo de confianza empleamos la función qt (inversa de la distribución)
# qt es la función que proporciona los percentiles de una distribucion
# t-Student para unos valores (en nuestro caso para alpha/2 y 1-alpha/2).
alpha <- 1-0.95
n <- length(muestra_tension)
intervalo_standard <- qt(c(alpha/2, 1-alpha/2), df=n-1)   
intervalo <- x_bar + s/2*intervalo_standard
print(x_bar)
print(s)
print(intervalo)


#########################################################################################

#######################
# 4) TESTS DE HIPÓTESIS
#######################

# Ejemplo de transparencias: test asociado a nivel de proteínas
#--------------------------------------------------------------
# H0: mu=7.25, H1: mu<>7.25
x_0=7.25

# Muestra
x= c(7.23,7.25,7.28,7.29,7.32,7.26,7.27,7.24)

# Calculamos los estadisticos x_barra, s, y el estadístico t_s del test
n <- length(x)
x_barra <- mean(x)
s <- sqrt(var(x))
t_s <- (x_barra-x_0)/(s/sqrt(n))
# Calculamos su p-valor recurriendo a la función de distribucion de la t-Student (pt)
p_valor <- 2*(1-pt(t_s, df=n-1))
print(p_valor)

# Comando unificado que calcula todo a partir de la muestra
# Proporciona también un intervalo de confianza (hemos elegido 95%) para la media 
t.test(x-7.25,alternative="two.sided",conf.level=0.95) 


# Ejemplo de transparencias: test sobre la varianza de altura de perros 
#----------------------------------------------------------------------
# H0: sigma^2=0.25, H1: sigma^2 < 0.25
# Valor de referencia de la varianza en H0
s_cuadrado_0 <- 0.25

# Datos muestrales
n <- 15
s_cuadrado <- 0.21
# Estadistico (que bajo H0 debe distribuirse como Chi-cuadrado)
estadistico <- (n-1)*s_cuadrado/s_cuadrado_0
# P-valor
pchisq(estadistico,n-1)
# Si tuvieramos los datos de la muestra y
#sigma.test(y, sigma = 0.25, sigmasq = sigma^2, alternative = c("two.sided", "less", "greater"), conf.level = 0.95, ...)


# Ejercicio 3 de hojas. Test asociado a proporción de sensores defectuosos
#-------------------------------------------------------------------------
# Proporcion habitual es 5%. Nuevo vendedor dice que la suya es menor del 5%
# Test: H0:p=0.05, H1: p<0.05 
p_0 <- 0.05

# Muestra
#Total
n <- 200
# Defectuosos
m <- 8

# Construir estadístico del test bajo H0
# Estimamos la proporción
p_hat <- m/n

# Estadístico (para muestra N>>40) bajo hipótesis H0 (Hipótesis de normalidad)
estadistico <- (p_hat-p_0)/sqrt(p_0*(1-p_0)/n)

# P-valor de la muestra
pnorm(estadistico)


# Ejercicio 4 de hojas. Nos dicen que la tensión arterial aceptable es 14 y 
# estamos preocupados (solamente) de que el paciente la tenga muy alta
# Test: H0:mu=14, H1: mu>14
#----------------------------------------------------
mu_0 <- 14

# Muestra
muestra_tension <- c(14.5,15.2,16,15.5)


# Calculamos los estadísticos muestrales
x_bar <- mean(muestra_tension)
s <- sd(muestra_tension)

# Región de aceptación (intervalo) para el test unilateral (en espacio normalizado)
alpha <- 1-0.95
region_aceptacion <- c(-Inf,qt(1-alpha,df=length(muestra_tension)-1))
print(region_aceptacion)

# P-valor del paciente
1-pt(2*(x_bar-mu_0)/s,df=length(muestra_tension)-1)

