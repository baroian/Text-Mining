# Text-Mining


### Data description

**NER features:**

*'O'* = Outside (not part of named entity)  

*'ART'* = Artefacts (objects)  

*'PER'* = Time Periods  

*'MAT'* = Materials  

*'LOC'* = Locations  

*'CON'* = Contexts  

*'SPE'* = Species

**Prefixes**

*'B-'*  Beginning token of a named entity

*'I-'* = Inside token of a named entity  

<br><br>


**Examples:**

<span style="font-size: 14px;">

"Medieval JJ B-PER

and CC O

post-medieval JJ B-PER

The DT B-LOC

Blue NNP I-LOC

Boar NNP I-LOC

Inn NNP I-LOC

( ( O

John NNP O "



<br>

*Note:*  the second token in a line is the POS (part of speeach) but it is not our target
</span>

