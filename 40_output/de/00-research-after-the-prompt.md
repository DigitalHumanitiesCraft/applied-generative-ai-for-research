---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/agentic-engineering-organises-multi-step-work]]", "[[30_assertions/applied-generative-ai-is-an-application-field]]", "[[30_assertions/frontier-models-amplify-asymmetrically]]", "[[30_assertions/neither-model-nor-prompt-alone-carries-the-work]]", "[[30_assertions/producing-an-artefact-is-not-judging-it]]", "[[30_assertions/research-data-are-constructed-representations]]", "[[30_assertions/the-four-engineering-layers-divide-the-field]]", "[[30_assertions/the-harness-mediates-between-the-layers]]", "[[30_assertions/the-prompt-is-one-component-of-the-loop]]", "[[30_assertions/the-translation-into-software-is-not-neutral]]", "[[30_assertions/three-levels-separate-holding-task-and-window]]"]
posits: 4
lang: de
part: Frame
chapter: 0
title: "Forschung nach dem Prompt"
feeding-sources: ["all parts of the feeding map"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Forschung nach dem Prompt

## Die Frage dieses Buches

Forschungsdaten sind ausgewählte und konstruierte Repräsentationen, die aus wissenschaftlicher Arbeit hervorgehen, und sie brauchen Dokumentation, Kontext und Sicherung, bevor sie eine Behauptung tragen können. Ein Faksimile, eine Transkription und eine ausgezeichnete Repräsentation derselben historischen Quelle sind deshalb nicht austauschbar, weil jede andere Möglichkeiten eröffnet und eine andere Form von Unsicherheit mitführt.[^0]

Untersuchbar werden solche Daten durch Software, und generische Software arbeitet auf der Ebene von Strukturen, die viele Projekte teilen. Eine Tabellenkalkulation erkennt eine Tabelle, eine Graphumgebung erkennt Knoten und Kanten, ein Editionsviewer erkennt einen Text und seinen Apparat. Keine von ihnen entscheidet, welche Unterscheidungen für eine bestimmte Forschungsfrage tragen, wie Unsicherheit dargestellt werden soll oder welche Interaktionsformen zu einer bestimmten wissenschaftlichen Praxis passen. Dieser Abstand zwischen dem, was Software erkennen kann, und dem, was ein Projekt sichtbar machen muss, ist der Ausgangspunkt dieses Buches.[^0a]

Generative Modelle verändern die technischen Bedingungen, unter denen projektspezifische Formen entstehen können. Eine Forscherin kann eine Datenstruktur beschreiben, eine Anforderung formulieren, Beispiele beisteuern und erhält daraus eine Transformation, eine Analyse oder ein Interface. Applied Generative AI bezeichnet das Feld, das diese Anwendung und Anpassung generativer Verfahren auf fachliche Probleme untersucht, und sein Gegenstand ist die Integration solcher Systeme in bestehende Wissenspraktiken samt den methodischen Folgen dieser Integration.[^1] Was dabei sinkt, ist der Aufwand manueller Formalisierung. Unberührt bleibt die Arbeit, das Material zu modellieren, auszuwählen, was das System sehen soll, zu spezifizieren, was es erzeugen soll, das Erzeugte zu prüfen und zu entscheiden, ob es eine Behauptung tragen kann.

Die zentrale Frage lautet deshalb nicht, ob generative Modelle nützliche Forschungsergebnisse hervorbringen. Sie lautet, wie sie in wissenschaftliche Arbeit eingebunden werden können, ohne die evidenziellen und interpretativen Grundlagen zu verdecken, von denen diese Ergebnisse abhängen. Die Fähigkeit, ein Artefakt zu erzeugen, und die Fähigkeit, es zu beurteilen, sind verschiedene Fähigkeiten, und ein Agent kann Ressourcen untersuchen, Informationen zusammenführen, Code erzeugen und ausführen und sich an Beobachtetes anpassen, ohne dass daraus folgt, ob das Ergebnis korrekt oder angemessen ist.[^2] Zu organisieren sind daher die Bedingungen, unter denen ein Ergebnis entsteht, geprüft, revidiert und für einen benannten Zweck verwendet wird.

## Warum der Prompt die falsche Einheit ist

Für eine abgegrenzte Aufgabe kann eine präzise formulierte Anweisung genügen. Extrahiere die Datumsangaben aus dieser Tabelle und gib sie strukturiert aus ist ein vollständiger Auftrag. Sobald eine Aufgabe mehrere Dateien, mehrere Werkzeuge und mehrere Entscheidungen umfasst, gehören die auftretenden Fragen nicht mehr einer Ebene an. Ein Teil betrifft die Gestaltung der aktuellen Aufgabe, ein Teil das persistente Projektwissen, ein Teil die Auswahl dessen, was das System vor Augen haben soll, und ein Teil die Kontrolle einer Ausführung, die über mehrere Schritte weiterläuft.[^3]

Dieses Buch folgt einer Aufteilung des Feldes in vier Ebenen. Prompt Engineering gestaltet die aktuelle Eingabesequenz. Knowledge Engineering baut und pflegt den verfügbaren Wissensbestand. Context Engineering stellt den Informationszustand zusammen, den eine konkrete Aufgabe verlangt. Agentic Engineering organisiert die mehrschrittige Ausführung innerhalb einer technischen Umgebung. Jede Ebene beantwortet eine andere Frage, wie die Aufgabe formuliert wird, was dokumentiert und gepflegt werden muss, welche Information das System jetzt braucht und wie die Arbeit organisiert, begrenzt und geprüft wird.[^4] Die Ebenen sind keine Phasen eines Ablaufs. Sie sind gleichzeitige Anliegen, und ein Projekt, das eine von ihnen gut gelöst hat, kann an einer anderen scheitern.

Zwischen ihnen vermittelt eine technische Umgebung. Sie stellt Werkzeuge und Zugriffe bereit, verwaltet den Zustand einer Arbeit und gibt Ergebnisse an das Modell zurück, und sie entscheidet nichts darüber, welche Lesart einer Quelle vertretbar ist oder ob ein Artefakt veröffentlicht werden darf.[^5] Diese Grenze sichtbar zu halten ist eine der wiederkehrenden Aufgaben des Buches, weil dieselbe Infrastruktur, die agentische Arbeit ermöglicht, es auch leicht macht, einen erfolgreichen Lauf für ein begründetes Ergebnis zu halten.

## Was das Buch beiträgt

Drei Begriffe tragen die Argumentation. Der erste ist eine persistente Wissensumgebung, in der Quellen, Daten, Projektwissen, Prozessgedächtnis, Instruktionen und Prüfmaterial versioniert und nachvollziehbar gehalten werden. Das Buch nennt sie Grounded Vault und entwickelt sie in Teil II. Ihr Kern ist die Unterscheidung zwischen einem Wissensbestand, der bleibt, und einem Informationszustand, der für eine Aufgabe zusammengestellt wird, eine Unterscheidung, die verhindert, dass Anhäufung an die Stelle von Auswahl tritt.[^6]

Der zweite ist Agentic Engineering als Form der Arbeitsorganisation. Er bezeichnet die systematische Organisation und Kontrolle mehrschrittiger agentischer Arbeit und umfasst die Abgrenzung und Zerlegung von Aufgaben, die Werkzeugnutzung, die Verarbeitung von Zwischenergebnissen, Übergaben, Abbruch- und Eskalationsbedingungen sowie Prüfung und Fortführung. Sein Gegenstand reicht über Code hinaus auf Datenbeschreibungen, Spezifikationen, Mappings, Designentscheidungen, Prozessdokumente und Verifikationskonzepte.[^7] Die Frage, die er an jede Anordnung stellt, lautet, unter welchen Bedingungen die Handlungen eines Agenten nachvollziehbar, begrenzt und korrigierbar bleiben.

Der dritte ist Promptotyping, eine iterative, dokumentenbasierte Methode, die Forschungsartefakte aus strukturierten Daten und wissenschaftlichen Spezifikationen ableitet und in Teil IV entwickelt wird. Ihre Arbeitseinheit ist ein versioniertes Dokumentenset und nicht eine einzelne Anweisung, und der Prompt ist eine operative Komponente in einem Zyklus, der von Projektwissen über einen Working Context und eine Implementation zu einer Prüfung führt, die das Projektwissen revidiert.[^8]

Nichts davon beschreibt einen Übergang zu autonomer Wissenschaft. Die Anordnung automatisiert keine neutrale Übersetzung von Forschungsdaten in Software. Sie macht jenen Teil der Übersetzung explizit, der formuliert, dokumentiert und geprüft werden kann, und die Verantwortung für die Interpretation der Daten, für die Angemessenheit der Modellierung und für die Akzeptanz eines Artefakts bleibt bei den für die Forschung verantwortlichen Personen.[^9]

## Vier leitende Fragen

Das Buch ist um vier Fragen herum angelegt.[^0b] Wie ordnen generative und agentische Systeme das Verhältnis von wissenschaftlichem Wissen, computationeller Ausführung und Prüfung neu? Wie muss Forschungswissen repräsentiert sein, damit es komplexe Arbeit über Modellinteraktionen hinweg tragen kann? Welche Verfahren erlauben es, inspizierbare Forschungsprozesse abzuleiten, ohne epistemische Autorität abzugeben? Unter welchen Bedingungen verstärkt Applied Generative AI die Forschungspraxis, und wo liegen ihre Grenzen?

Die vierte Frage hat eine Antwort, die die übrigen prägt. Die Verstärkung ist ungleich verteilt. Sie konzentriert sich dort, wo die relevante Information digital repräsentiert ist, wo Handlungen über Software ausgeführt werden können und wo die Umgebung brauchbare Rückmeldung liefert, und sie hängt von vorhandener Expertise, zugänglichen Daten, technischer Infrastruktur und der Fähigkeit zur Beurteilung eines Ergebnisses ab. Dasselbe System erweitert deshalb verschiedene Praktiker in sehr verschiedenem Maß.[^10] Ein Buch über Methode muss das früh sagen, weil eine Methode, die gleichmäßigen Nutzen unterstellt, für eine Leserschaft geschrieben wäre, die es nicht gibt.

## Zum Aufbau

Teil I behandelt generative Modelle als Forschungssysteme und fragt, was ein Modell ist, was das System um es herum beiträgt und welchen Status seine Ausgaben haben. Teil II verfolgt den Weg vom Prompting über Context Engineering und Knowledge Engineering zum Grounded Vault. Teil III behandelt agentische Arbeit, ihre Organisation und ihre Fehlerformen. Teil IV entwickelt Promptotyping als Methode, Teil V untersucht Forschungsartefakte und vergleichende Fälle, Teil VI arbeitet ein vollständiges Beispiel und die Grenzen des Ansatzes durch. Die Reihenfolge ist im Vokabular kumulativ, während der Schwierigkeitsgrad in etwa gleich bleibt, sodass wer an Datenmodellierung arbeitet in Teil II einsteigen kann und wer bereits agentische Workflows betreibt bei Teil III beginnen kann. Jedes Kapitel benennt die Assertions, auf denen es ruht, sodass eine Behauptung bis zur tragenden Quellenstelle verfolgt werden kann.[^0c]

## Lücken

Dieses Kapitel stützt sich auf das Lehrmaterial des Projekts und auf den Foliensatz, und drei Dinge, die es braucht, liegen anderswo.[^11]
- Der Grounded Vault wird hier über seine Funktion eingeführt und in Kapitel 7 vollständig bestimmt. Seine Governance-Bedingung ruht in den Quellen auf einer Forderung nach Provenienz und nicht auf einer Architektur, die sie durchsetzt, und die Ankerkette dieses Buches ist die eigene Erweiterung dessen, was die Quellen beschreiben.
- Die Charakterisierung von Promptotyping bleibt bewusst dünn, weil das Paper, das die Methode definiert, zur anderen Manuskriptlinie gehört und sein Destillat der Anker für Teil IV ist.
- Die Aussage, dass Forschungsdaten bereits selektive Repräsentationen sind, entfaltet Kapitel 3 aus den englischen Lecture Notes; sie würde tragfähiger mit einer Quelle aus der Forschungsdatenliteratur, die als eigener Publikationsdatensatz aufgenommen wird.

[^0]: Grounded in [[30_assertions/research-data-are-constructed-representations]].
[^0a]: Posit: die Grenze generischer Software ist hier aus der Praxis der Projekte formuliert, auf die sich dieses Buch stützt, und aus keiner Messung. Open evidence question: ein Vergleich dessen, was ein Projekt sichtbar machen muss, mit dem, was eine Allzweckumgebung freilegt, über mehrere Fächer hinweg.
[^0b]: Posit: die vier Fragen sind der Rahmen, den die Autorenschaft für das Buch setzt. Open evidence question: ob die Teile in ihrer ausgearbeiteten Form sie beantworten, was erst das fertige Manuskript entscheidet.
[^0c]: Posit: die Lesereihenfolge ist eine Empfehlung. Open evidence question: ob Lesende, die bei Teil II oder III einsteigen, das nötige Vokabular mitbringen, was die Lehrfälle in Teil V prüfen könnten.
[^1]: Grounded in [[30_assertions/applied-generative-ai-is-an-application-field]].
[^2]: Grounded in [[30_assertions/producing-an-artefact-is-not-judging-it]].
[^3]: Grounded in [[30_assertions/neither-model-nor-prompt-alone-carries-the-work]].
[^4]: Grounded in [[30_assertions/the-four-engineering-layers-divide-the-field]].
[^5]: Grounded in [[30_assertions/the-harness-mediates-between-the-layers]].
[^6]: Grounded in [[30_assertions/three-levels-separate-holding-task-and-window]].
[^7]: Grounded in [[30_assertions/agentic-engineering-organises-multi-step-work]].
[^8]: Grounded in [[30_assertions/the-prompt-is-one-component-of-the-loop]].
[^9]: Grounded in [[30_assertions/the-translation-into-software-is-not-neutral]].
[^10]: Grounded in [[30_assertions/frontier-models-amplify-asymmetrically]].
[^11]: Posit: die Lückenliste ist das Urteil der Autorenschaft darüber, was dieses Kapitel noch nicht tragen kann. Open evidence question: ob das Destillat des Promptotyping-Papers aus der anderen Manuskriptlinie die zweite Lücke schließt oder weitere öffnet.
