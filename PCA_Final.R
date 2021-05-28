setwd("~/Documents/Dissertation/R")

data<- read.csv("data_df_mt_003.csv")
res.pca <- prcomp(data,center = TRUE, scale. = TRUE)
#res.pca <- PCA(data, graph = FALSE)
summary(res.pca)
head(data)
print(res.pca)


#Eigenvalues / Variances
library(factoextra)
eig.val <- get_eigenvalue(res.pca)
eig.val

#Export info to csv
spc <- data.frame(summary(res.pca)$importance)
ppc <- data.frame(res.pca$rotation)
write.csv(spc, "~/Documents/Dissertation/R/spc.csv")
write.csv(ppc, "~/Documents/Dissertation/R/ppc.csv")

######Graph of variables

#Scree Plot
fviz_eig(res.pca, addlabels = TRUE, ylim = c(0, 50))

##Results
var <- get_pca_var(res.pca)
var$contrib
coord <- data.frame(var$coord)
write.csv(coord, "~/Documents/Dissertation/R/coord.csv")

# Coordinates
head(var$coord)
# Cos2: quality on the factore map
head(var$cos2)
# Contributions to the principal components
head(var$contrib)

#Correlation circle
head(var$coord)
fviz_pca_var(res.pca, col.var = "black")

#Contributions of variables to PCs
fviz_contrib(res.pca, choice = "var", axes = 1, top = 10)
fviz_contrib(res.pca, choice = "var", axes = 2, top = 10)
fviz_contrib(res.pca, choice = "var", axes = 3, top = 10)
fviz_contrib(res.pca, choice = "var", axes = 4, top = 10)
fviz_contrib(res.pca, choice = "var", axes = 5, top = 10)

fviz_contrib(res.pca, choice = "var", axes = 1:2, top = 10)



#Color by a custom continuous variable
fviz_pca_var(res.pca, col.var = "contrib",
             gradient.cols = c("#00AFBB", "#E7B800", "#FC4E07")
)

#Source Link
##http://www.sthda.com/english/articles/31-principal-component-methods-in-r-practical-guide/112-pca-principal-component-analysis-essentials/#biplot