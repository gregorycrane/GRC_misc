# The seven surviving plays of Aeschylus
# Literal translations and context-aware glosses produced by Gemini 3
# Based on the Francesco Mambrini Treebanks
November 27, 2025

TL/DR: We are looking for people to look at the literal translations and context-aware glosses of Aeschylus in this directory. Please report your findings as a Github issue [here](https://github.com/gregorycrane/GRC_misc/issues/3).

In late November 2027, we provided the newly released Gemini 3 model with the following prompt:


> You are extending an existing Treebank in two ways. First, you are creating a sentence by sentence translation that follows the syntactic analysis in the Treebank. Second, you are adding context-aware glosses to each word in the Treebank.


The results for all seven surviving plays traditionally attributed to Aeschylus are available in this github directory [here](https://github.com/gregorycrane/GRC_misc/tree/main/aesch/AeschTBTrans).


The translations presented are in English but the English translations are offered as a proof of concept. By starting with a treebank and with explicit grammatical analysis, our hope is that we will be able to generate consistent, literal translations into a wide variety of languages. A next step in this rseearch would be to generate and evaluate translations into a range of other modern languages.

Aeschylus is one of the most difficult Greek texts to translate. Our hypothesis is that access to the Treebanks will have improved the ability of the model to produce consistent translations. We expect an error rate.

Note also: the Gemini 3 translations and glosses are presented as a first draft with which to get started. The translations are fully in the public domain and the idea is to modify them as people see fit. For now we are assessing this initial automatically generated version.

Literal translations designed to illustrate the underlying Greek and context-aware glosses are fundamental elements to any modern edition of an historical text. The goal is to open the Greek up to the widest possible audience -- ideally to a global audience. Translation -- and particularly literal translation -- is a necessary (though not sufficient) instrument in a system designed to open up the source text. 

In this case, the translations are unusual in that they are built upon a preexisting word-by-word morphological and syntactic analysis of the source text. We refer to such richly annotated texts as Treebanks because the syntactic structure, when visualized, resembles an inverted tree, with root at the top and branches extending downwards. Francesco Mambrini originally produced these treebanks when working at the Perseus Digital Library in the late 2000s. The treebanks here reflect three layers of work.


* The Oresteia and the Prometheus were converted to the Universal Dependency Framework and are available in the [Daphne Repository](https://github.com/francescomambrini/Daphne/tree/master/data/annotation/latest).

* The Suppliant Women, Persians and Seven Against Thebes have not been updated. We used the treebanks for these plays that are available under the older Perseus Dependency Treebank Guidelines. The treebanks are available [here](https://github.com/PerseusDL/treebank_data/tree/master/v1.6/greek/data). They reflect a version where conversion from betacode into unicode produced artifacts (mainly apostrophes interpreted as breathing marks). We can clean these up when we align the treebank to other editions.

* The final lines (945ff.) of the Libation Bearers were not treebanked. To patch this gap in the short run (and thus to get a first draft of the whole corpus), we loaded the first 944 lines of the Libation Bearers treebank into Gemini 3 and asked it to use that as a model to treebank, translate and gloss the remaining lines.