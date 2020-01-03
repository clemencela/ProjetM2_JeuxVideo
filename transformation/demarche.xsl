<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" encoding="utf-8"/>
<xsl:template match="/">

<html>
	<head>
	    <!-- on appelle le template pour le titre de l'onglet -->
		<xsl:apply-templates select="page/head_logo/titre_onglet"/>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
	</head>
	<body class="no-sidebar is-preload">
		<div id="page-wrapper">

			<!-- Header Wrapper -->
				<div id="header-wrapper">
					<div class="container">

						<!-- Header -->
							<header id="header">
								<div class="inner">

									<!-- Logo -->
										<!-- on appelle le template pour le titre de la bannière -->
										<xsl:apply-templates select="page/head_logo/titre_banniere"/>

									<!-- Nav -->
										<nav id="nav">
											<ul>
												<li><a href="index.html">Accueil</a></li>
												<li class="current_page_item"><a href="demarche.xml">Démarche</a></li>
												<li>
													<a href="#">Résultats</a>
													<ul>
														<li><a href="basique.html">Basique</a></li>
														<li><a href="ventes.html">Ventes</a></li>
														<li><a href="critique.html">Critique et ventes</a></li>
														<li><a href="esrb.html">ESRB et ventes</a></li>
													</ul>
												</li>
												<li><a href="remarques.html">Remarques</a></li>
												
											</ul>
										</nav>

								</div>
							</header>

					</div>
				</div>

			<!-- Main Wrapper -->
				<div id="main-wrapper">
					<div class="wrapper style2">
						<div class="inner">
							<div class="container">
								<div id="content">

									<!-- Content -->

										<article>
											<!-- on appelle le template pour l'élément démarche -->
											<xsl:apply-templates select="page/demarche"/>
											<div align="center"><a href="demarche.xml" class="button medium icon solid fa-arrow-circle-right">Haut de la page</a></div>
											
										</article>

								</div>
							</div>
						</div>
					</div>
					
				</div>

			<!-- Footer Wrapper -->
				<div id="footer-wrapper">
					<footer id="footer" class="container">
						<div class="row">
							
							<div class="col-12">
								<div id="copyright">
									<ul class="menu">
										<!-- Code de l'entité copyright -->
										<li>&#169; Les jeux vidéos en chiffres. All rights reserved</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
									</ul>
								</div>
							</div>
						</div>
					</footer>
				</div>

		</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.dropotron.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>
</xsl:template>
<!-- Description des différents template -->
<!-- Template pour le titre de l'onglet
	On récupère ce que contient l'élément pour le mettre
	entre deux balises html title -->
<xsl:template match="page/head_logo/titre_onglet">
<title><xsl:value-of select="."/></title>
</xsl:template>

<!-- Template pour le titre de la bannière 
	On récupère ce que contient l'élément pour le mettre
	entre deux balises html h1 -->
<xsl:template match="page/head_logo/titre_banniere">
<h1><a href="index.html" id="logo"><xsl:value-of select="."/></a></h1>
</xsl:template>

<!-- Template pour l'élément demarche 
	On récupère la valeur de l'attribut titre pour la mettre
	entre deux balises html h2 -->
<xsl:template match="page/demarche">
<header class="major"><h2><xsl:value-of select="./@titre"/></h2></header>
<!-- On s'occupe des éléments etape contenus dans demarche
	On récupère la valeur de l'attribut titre pour la mettre
	entre deux balises html h3 -->
<xsl:for-each select="./etape">
<h3><xsl:value-of select="./@titre"/></h3>
<!-- On s'occupe des éléments contenu à l'intérieur des éléments etape 
	Si l'attribut type est texte, alors on affiche la valeur de l'élément contenu dans une balise html p
	Si l'attribut type est liste, alors on affiche les valeurs des éléments element_liste dans une structure html de liste 
	Si l'attribut type est liste_para, alors on suit la même logique mais avec un autre type de liste
	Si l'attribut type est doc, alors on affiche dans un lecteur pdf intégré à la page le document dont le chemin est spécifié dans l'attribut chemin
	Si l'attribut type est image, alors on affiche l'image dont le chemin est spécifié dans l'attribut chemin grâce aux bonnes balises html
	Enfin, si l'attribut type est titre, alors on affiche la valeur de l'élément contenu dans une balise html h4 -->
<xsl:for-each select="./contenu">
<xsl:if test="./@type = 'texte'">
<p align="justify"><xsl:value-of select="."/></p>
</xsl:if>
<xsl:if test="./@type = 'liste'">
<ul class="default">
<xsl:for-each select="./element_liste">
<li><xsl:value-of select="."/></li>
</xsl:for-each>
</ul>
</xsl:if>
<xsl:if test="./@type = 'liste_para'">
<ul class="dif">
<xsl:for-each select="./element_liste">
<li><xsl:value-of select="."/></li>
<p></p>
</xsl:for-each>
</ul>
</xsl:if>
<xsl:if test="./@type = 'doc'">
<center><embed width="800" height="550" type='application/pdf'><xsl:attribute name="src"><xsl:value-of select="./@chemin"/></xsl:attribute></embed></center>
<p></p>
</xsl:if>
<xsl:if test="./@type = 'image'">
<center><span class="image fit"><img alt=""><xsl:attribute name="src"><xsl:value-of select="./@chemin"/></xsl:attribute></img></span></center>
<p></p>
</xsl:if>
<xsl:if test="./@type = 'titre'">
<h4><xsl:value-of select="."/></h4>
</xsl:if>
</xsl:for-each>
</xsl:for-each>
</xsl:template>
</xsl:stylesheet>