---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-prompt-is-a-bounded-specification]]", "[[30_assertions/a-prompt-is-the-whole-input-sequence]]", "[[30_assertions/iteration-runs-in-bounded-passes]]", "[[30_assertions/no-single-prompting-strategy-is-optimal]]", "[[30_assertions/personas-produce-hypotheses]]", "[[30_assertions/precision-does-not-follow-from-length]]", "[[30_assertions/prompt-effects-are-local]]", "[[30_assertions/prompt-engineering-is-iterative-design-and-evaluation]]", "[[30_assertions/prompt-variants-are-experimental-interventions]]", "[[30_assertions/prompting-does-not-replace-work-organisation]]", "[[30_assertions/prompting-intervenes-in-the-current-computation]]", "[[30_assertions/role-assignment-adds-no-domain-knowledge]]", "[[30_assertions/structured-output-has-four-levels-of-conformance]]", "[[30_assertions/the-object-shifts-to-the-information-state]]"]
posits: 1
lang: de
part: "II. Vom Prompting zum grundierten Wissen"
chapter: 4
title: "Prompting und Prompt Engineering"
topic: "[[Grounded-Knowledge]]"
feeding-sources: ["script chapters 3 to 5", "paper (Project Knowledge Base)", "Vault als materialisiertes Wissensmodell"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Prompting und Prompt Engineering

## Was ein Prompt ist

Ein Prompt ist die gesamte Eingabesequenz, die für einen Modellaufruf bereitgestellt wird. Sie kann eine Aufgabe, Ausgangsmaterial, Kontextinformationen, Anforderungen, Einschränkungen, Beispiele, Verfahrenshinweise und Vorgaben zur erwarteten Ausgabe enthalten, sodass die Lesart als Frage das meiste verdeckt, was tatsächlich übergeben wird.[^1] Das Wort legt das falsche Bild nahe, eine an ein Gegenüber gerichtete Formulierung, während der Gegenstand eine Datenstruktur ist, deren Teile verschiedene Funktionen haben.

Prompt Engineering ist die iterative Gestaltung und Bewertung einer solchen Sequenz für ein bestimmtes Modell und eine bestimmte Aufgabe. Die Arbeit verläuft über Veränderungen an Inhalt, Struktur oder angewandter Technik und die Bewertung des Ergebnisses, und der Begriff bleibt bewusst enger als Context Engineering, weil er eine Eingabesequenz betrifft und nicht die gesamte Informationsumgebung einer längeren Arbeitstrajektorie.[^2] Kapitel 5 übernimmt dort, wo diese Enge aufhört zu tragen.

## Der Prompt als begrenzte Spezifikation

Produktiv ist die Form einer begrenzten Spezifikation innerhalb eines bereits vorhandenen Wissens- und Arbeitskontextes. Ihre typischen Bestandteile sind Ziel, Ausgangslage, Anforderungen, Einschränkungen, Vorgehen, Ausgabeform und Abschlusskriterium, und die Trennung der aktuellen Aufgabe von Quellenkontext, Regeln und Ausgabevertrag macht jeden Teil für sich prüfbar. Die Kategorien lassen sich unabhängig voneinander verändern, sodass eine andere Quelle den Kontext und eine andere editorische Regelung die Regeln ändert, was die Anordnung zu einer transparenten Trennung macht und nicht zu einer universellen Vorlage.[^3]

Länge ist hier das falsche Qualitätsmaß. Ein sehr langer Prompt kann widersprüchlich oder schwer priorisierbar sein, und ein kurzer genügt, wenn die einschlägigen Regeln bereits in Wissensdokumenten und Instruktionsdateien stehen, sodass ein Aufgabenprompt, der auf den persistenten Bestand verweist statt ihn zu wiederholen, kompakt bleibt. Was eine begrenzte Formulierung erreicht, ist eine geringere Zahl stiller Annahmen, und sie garantiert kein korrektes Ergebnis.[^4]

Rollen sind ein Sonderfall, der genaue Formulierung verdient. Eine Rollenzuweisung kann Terminologie, Stil, Perspektive und Detaillierungsgrad beeinflussen, indem sie gelernte Muster fachsprachlicher Kommunikation wahrscheinlicher macht, und sie fügt kein Fachwissen hinzu. Eine knappe funktionale Zuweisung und eine ausgearbeitete Persona mit Hintergrund, Erfahrung, Zielen und Nutzungssituation gehören zusammen betrachtet, ohne dass sie dasselbe Instrument wären, und Rollen bleiben nützlich, wo eine Aufgabe tatsächlich eine bestimmte Perspektive, Adressierung oder Bewertungshaltung verlangt.[^5]

Eine synthetische Persona erzeugt Hypothesen über Nutzende. Sie kann mögliche Probleme sichtbar machen und eine konsistente Perspektive definieren, aus der ein Artefakt geprüft wird, und ihre Antworten sind gegen reale Personen, Beobachtungen oder vorhandene Nutzerforschung zu prüfen. Personas eignen sich für Stilvariation, Perspektivwechsel, frühe Materialkritik, die Vorbereitung von Interviews und das Auffinden wahrscheinlicher Rückfragen, und sie ersetzen weder Fachwissen noch reale Stakeholder, empirische Forschung oder fachliche Validierung.[^6]

## Warum Prompting-Befunde nicht wandern

Die empirische Literatur zu Promptwirkungen ist auf eine Weise heterogen, die selbst der Befund ist. Untersuchungen berichten Effekte emotionaler Zusätze, von Höflichkeit und ungewöhnlicher automatisch erzeugter Prompts, während andere Arbeiten zeigen, dass irrelevante Zusätze die Leistung verschlechtern oder dass Effekte auf neueren Modellen nicht stabil replizieren. Ein verändertes Ergebnis nach einer Variation zeigt nicht, dass die Formulierung aus dem angenommenen Grund wirkt, und Effekte einer Modellgeneration können in der nächsten schwächer werden, verschwinden oder sich umkehren.[^7] Diese Instabilität erzeugt die Zahl der beteiligten Faktoren, Modell und Version, Aufgabe und Datensatz, Sprache, Position und Struktur der Information, Evaluationsmetrik und Zufallsvariation.

Daraus folgen zwei Dinge. Das erste ist prozedural. Eine Promptvariante ist eine experimentelle Intervention und wird als solche bewertet, indem Ziel und Metrik festgelegt, eine Baseline definiert, nur ein relevanter Bestandteil verändert, mehrere Beispiele und Wiederholungen verwendet, neue Fälle geprüft, Modell und Version dokumentiert und fachliche Qualität getrennt von Stil und Format beurteilt werden.[^8] Das zweite ist eine Grenze der Verallgemeinerung. Keine einzelne Strategie ist über Modelle, Aufgaben und Bewertungssituationen hinweg optimal, sodass wirksames Prompting eine Kombination aus Kontextauswahl, Anweisungsgestaltung, Inferenzstrategie und Bewertung ist und keine gefundene Formulierung.[^9]

Eine verwandte Disziplin gilt für Ausgabeformate. Die Forderung nach einem strukturierten Format verringert Mehrdeutigkeit, und die Ebenen, die sie entscheiden kann, sind begrenzt. Syntaktische Konformität, strukturelle Vollständigkeit, semantische Richtigkeit und wissenschaftliche Angemessenheit sind getrennte Fragen, und eine Formatvorgabe reicht bis zur zweiten.[^10] Iteration hilft aus demselben Grund. Ein produktiver Austausch läuft über begrenzte Durchgänge aus Erzeugen, Prüfen, Korrigieren und Verdichten, und die Trennung des Durchgangs, der Befunde findet, von dem, der sie behebt, hält beide beurteilbar.[^11]

## Wo der Prompt endet

Prompt Engineering präzisiert eine aktuelle Aufgabe. Es löst für sich weder fehlendes oder unzugängliches Projektwissen, widersprüchliche Richtlinien, ungeklärte Anforderungen, einen überladenen Kontext, fehlende Dokumentation, Werkzeug- und Berechtigungsverwaltung, technische Tests noch fachliche Validierung, und es organisiert keine längere Arbeitstrajektorie.[^12] Jedes dieser Probleme ist von anderer Art, und ein Projekt, das sie durch Umformulieren einer Anweisung zu lösen versucht, erzeugt längere Anweisungen und dieselben Defekte.

Der Gegenstand der Gestaltung verschiebt sich deshalb. Komplexe Arbeit enthält mehr relevante Information, als in einen einzelnen Prompt gehört, weil Ziele, Dokumente, Daten, Vorgaben, Anforderungen, Beispiele, Designentscheidungen, frühere Befunde, offene Fragen und Prüfkriterien alle zählen, ohne gleichzeitig zu zählen, und die Gestaltungsfrage wandert von der Formulierung einer Anweisung dorthin, was verfügbar ist, wie es repräsentiert wird, in welcher Reihenfolge es erscheint, was nachgeladen werden kann und was bewusst wegbleibt.[^13]

Ein weiterer Grund für diese Verschiebung stammt aus Kapitel 1. Wenn ein Prompt ein Eingriff in die Berechnung ist, die das Modell gerade ausführt, dann bedingt die gesamte Sequenz diese Berechnung, und die Anweisung ist ein Teil der Sequenz neben dem Material, den Beispielen und dem angesammelten Verlauf.[^14] Wer die Anweisung verbessert und den Rest ungeordnet lässt, optimiert einen Bruchteil dessen, was das Ergebnis bestimmt.

## Lücken

Zwei Themen der Gliederung sind hier dünner behandelt, als die Gliederung vorsieht.[^15]
- Prompt-Versionierung nennt die Gliederung, und in den Quellen erscheint sie nur innerhalb des experimentellen Verfahrens als Forderung, Modell und Version zu dokumentieren. Eine Praxis, Prompts als Projektartefakte zu versionieren, verlangt die Promptotyping-Vorlagen der anderen Manuskriptlinie.
- Zero-Shot- und Few-Shot-Prompting als benannte Techniken kommen in den Quellen dieser Arbeitslinie nicht vor; sie behandeln Beispiele als einen Bestandteil der Eingabesequenz ohne diese Terminologie. Die Überblicksliteratur, die die Quellen zitieren, müsste als Publikationsdatensatz aufgenommen werden, bevor die Begriffe verwendbar sind.

[^1]: Grounded in [[30_assertions/a-prompt-is-the-whole-input-sequence]].
[^2]: Grounded in [[30_assertions/prompt-engineering-is-iterative-design-and-evaluation]].
[^3]: Grounded in [[30_assertions/a-prompt-is-a-bounded-specification]].
[^4]: Grounded in [[30_assertions/precision-does-not-follow-from-length]].
[^5]: Grounded in [[30_assertions/role-assignment-adds-no-domain-knowledge]].
[^6]: Grounded in [[30_assertions/personas-produce-hypotheses]].
[^7]: Grounded in [[30_assertions/prompt-effects-are-local]].
[^8]: Grounded in [[30_assertions/prompt-variants-are-experimental-interventions]].
[^9]: Grounded in [[30_assertions/no-single-prompting-strategy-is-optimal]].
[^10]: Grounded in [[30_assertions/structured-output-has-four-levels-of-conformance]].
[^11]: Grounded in [[30_assertions/iteration-runs-in-bounded-passes]].
[^12]: Grounded in [[30_assertions/prompting-does-not-replace-work-organisation]].
[^13]: Grounded in [[30_assertions/the-object-shifts-to-the-information-state]].
[^14]: Grounded in [[30_assertions/prompting-intervenes-in-the-current-computation]].
[^15]: Posit: die Lückenliste hält fest, wo dieses Kapitel hinter der Gliederung zurückbleibt. Open evidence question: ob das Vorlagenset der anderen Manuskriptlinie eine Praxis der Prompt-Versionierung trägt oder nur eine Dokumentversionierung.
