---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-finding-is-attributed-before-it-is-written-back]]", "[[30_assertions/a-public-deployment-is-the-latest-state-of-a-development-history]]", "[[30_assertions/a-reproducible-metric-does-not-validate-its-own-specification]]", "[[30_assertions/an-artefact-alone-does-not-witness-its-own-history]]", "[[30_assertions/conformity-to-a-mapping-is-examined-separately-from-its-adequacy]]", "[[30_assertions/data-production-becomes-accountable-through-a-reconstructable-relation]]", "[[30_assertions/distillation-preserved-uncertainty-and-negative-findings]]", "[[30_assertions/early-interfaces-make-a-model-discussable-through-operations]]", "[[30_assertions/formal-modelling-does-not-determine-the-operational-form]]", "[[30_assertions/four-analytical-dimensions-organise-the-comparison]]", "[[30_assertions/implementation-can-participate-in-the-formation-of-a-model]]", "[[30_assertions/inspection-is-separated-from-the-authority-to-record]]", "[[30_assertions/interaction-exposes-unwarranted-precision]]", "[[30_assertions/interface-findings-concern-the-claims-a-representation-implies]]", "[[30_assertions/project-level-and-method-level-write-back-differ]]", "[[30_assertions/prompt-borne-metadata-can-enter-a-transcription]]", "[[30_assertions/purpose-specific-acceptance-bounds-the-claim]]", "[[30_assertions/the-cases-are-reconstructions-under-a-common-analytical-structure]]", "[[30_assertions/the-cases-share-a-relation-and-not-a-chronology]]", "[[30_assertions/the-documented-corpus-spans-conditions-and-purposes]]"]
posits: 1
lang: de
part: "V. Research Artefacts and Comparative Cases"
chapter: 19
title: "Vergleichende Projektfälle"
topic: "[[Research-Artefacts]]"
feeding-sources: ["paper chapters 2.3 and 3"]
working-title: true
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Vergleichende Projektfälle

## Was der Vergleich tragen kann

Die folgenden Fälle sind methodisch geleitete Rekonstruktionen dokumentierter Projektpraxis und keine vollständigen Geschichten oder Erfolgsgeschichten, und jeder wird über dieselben Elemente gelesen, also über seinen Ausgangszustand, das Zusammenspiel der vier Arbeitsformen, die aus der Implementierung entstandenen Befunde und deren Einarbeitung in revidiertes Projektwissen oder in eine zweckgebundene Abnahme.[^1] Der Vergleich ist über vier Dimensionen organisiert, die Projektbedingung, aus der die Implementation begann, die primäre methodische Funktion, die sie erfüllte, die operative Form des entstandenen Artefakts und die Ebene, auf der die Prüfung einen folgenreichen Befund erzeugte, und diese Dimensionen können sich überschneiden und zwischen Iterationen wechseln.[^2]

Eine Einschränkung regiert das ganze Kapitel. Eine öffentliche Oberfläche oder ein lauffähiges Artefakt belegt, dass ein bestimmter Implementierungsstand existierte, und zeigt, welche Operationen er bereitstellte, und es belegt für sich weder die Geschichte dieses Standes noch die Entscheidungen, die zu ihm führten, noch die zurückgeschriebenen Befunde, noch die Autorität, über die Verifikation oder Abnahme zugewiesen wurde, weshalb jede Aussage über Entwicklung, Revision, Prüfung und Abnahme an die erhaltene Dokumentation gebunden bleibt.[^3] Manche Projekte bewahren umfangreiche Aufzeichnungen, andere sind vor allem durch ein Artefakt und einen begrenzten Dokumentensatz repräsentiert, weshalb der Vergleich dokumentierte Muster benennt und nicht jedes Projekt gleich genau rekonstruiert.

## Semantische Explizitheit und aufgabenspezifischer Kontext

Die erste Gruppe betrifft Projekte, die ihre Semantik formal explizit gemacht haben und dann feststellten, dass Explizitheit das Artefakt unterbestimmt lässt. Ein gemeinsames Modell historischer Buchhaltungstransaktionen normalisierte heterogene Datensätze und trug zwei gegensätzliche Untersuchungen, eine, die soziale Beziehungen und Austauschformen über wirtschaftliche Transaktionen verfolgte, und eine, die über administrative und zeitliche Hierarchien aggregierte und verglich. Die interoperable Repräsentation trug beide Untersuchungsformen und bestimmte weder, welche Unterscheidungen in den Vordergrund gehörten, noch, welche Operationen und Interfacestrukturen jede von ihnen verlangte.[^4]

Für die Methode folgt daraus, dass formale Semantik eine Bedingung projektspezifischer Arbeit ist und kein Ersatz für sie. Die Aufbereitung der Daten stützt Maschinenverarbeitbarkeit, Interoperabilität und Nachnutzung, und die operative Form ist weiterhin gegen die jeweilige Frage zu entscheiden.[^4] Die Fälle dieser Gruppe zeigen Kontextkonstruktion damit als eine Aufgabe, die Standardisierung überdauert, und sie verorten die folgenreichen Befunde auf der Ebene des Modells und seiner intendierten Nutzung.

## Forschungsartefakte als Repräsentationen

Die zweite Gruppe betrifft Artefakte, deren Repräsentationsentscheidungen selbst zum Prüfgegenstand wurden. Eine Explorationsumgebung für Korrespondenz zeigte mit frühestem und spätestem Datum kodierte Angaben als präzise Punkte auf einer Zeitleiste, was eine Präzision behauptete, die die Datensätze nicht trugen, und die Korrektur stellte sie als Intervalle dar und ließ die Datensätze unberührt.[^5] Ein Projekt, dessen Datenmodell, Vokabular und Erfassungspraxis noch in Entwicklung waren, nutzte frühe Oberflächen, damit Beteiligte Information in einer gemeinsamen operativen Umgebung eingeben, anzeigen, filtern und vergleichen konnten, sodass sich Kategorien, Relationen und Erfassungsanforderungen an den ihnen zugewiesenen Datensätzen prüfen ließen statt allein an Schemata.[^6]

In diesem zweiten Projekt nahm das Artefakt an der Bildung des Modells teil, das es implementierte, was unter der Bedingung galt, dass die durch die Nutzung offengelegten Folgen interpretiert, dokumentiert und in das gepflegte Projektwissen eingearbeitet wurden.[^7] Der Interpretationsschritt macht das methodische Interesse dieser Gruppe aus, denn manche Befunde betrafen die repräsentierte Domäne und verlangten eine Revision von Datenmodell oder Erfassungspraxis, während andere die Zugänglichmachung einer im Übrigen angemessenen Unterscheidung betrafen und im Design der Oberfläche bleiben konnten.[^8] Die Interaktion legte außerdem offen, wo eine technisch mögliche Visualisierung ein Maß an Präzision, Vollständigkeit oder Sicherheit unterstellt hätte, das die Daten nicht decken.[^9]

## Generative Verarbeitung und Prüfung

Die dritte Gruppe betrifft Pipelines, die Forschungsdaten mit generativen Komponenten herstellen und Produktion von Autorisierung trennen müssen. Zwei Transkriptions- und Kodierungsworkflows, einer an handschriftlichem Nachlassmaterial und einer an digitalisierten gedruckten Schriften an einer wissenschaftlichen Bibliothek, überführten heterogene mehrsprachige Quellen in strukturierte textuelle Forschungsdaten und hielten erzeugte Outputs und Zwischenzustände für Prüfung und Korrektur verfügbar.[^10]

Drei Befunde dieser Gruppe reichen über ihre Projekte hinaus. Ein kontrollierter Vergleich zeigte, dass reichere Prompt-Metadaten Information in eine Transkription tragen konnten, die im Bild nicht sichtbar war, was ein Fehlermodus der Kontextanreicherung ist und keiner des Modells.[^11] Ein Agent-Screening vergab Freigabelabel, obwohl keine verantwortliche Person eine Freigabe erteilt hatte, die Label wurden abgeschafft, und die Befunde wurden als vorläufige Evidenz bis zur Adjudikation neu eingestuft, womit feststand, dass die Fähigkeit, einen Output zu prüfen, und die Autorität, ihn als verifiziert festzuhalten, getrennt sind.[^12] Und die Verwendung einer Character Error Rate zeigte, dass eine reproduzierbare Metrik die Abweichung von einer gewählten Referenz misst und nicht die Korrektheit einer Transkription, sodass die Wahl der Referenz und die Behandlung textueller Phänomene editorische Entscheidungen innerhalb einer scheinbar technischen Zahl bleiben.[^13]

Das gepflegte Wissen dieser Workflows hielt Eigenschaften des Materials, Verarbeitungsanforderungen, Annotations- und Prüfkonventionen, methodische Entscheidungen, offene Fragen und Gründe für die Revision früherer Ansätze fest, einschließlich der Phänomene, die das verfügbare Referenzmaterial nicht repräsentiert und daher als Vergleichsgrundlage nicht tragen kann.[^14] Ihre Repositorien bewahren zudem die Alternativen, die geprüft, eingeschränkt, ersetzt oder verworfen wurden, was die öffentlichen Deployments zu den jeweils jüngsten prüfbaren Ständen dokumentierter Entwicklungsgeschichten macht.[^15] Verantwortbarkeit ruht in dieser Gruppe auf dem rekonstruierbaren Verhältnis von Quellen, gepflegtem Wissen, versionierter Implementierung, differenzierter Evidenz und verantwortlichem Urteil, und die Bedeutung der Workflows liegt ebenso in verworfenen Annahmen, entdeckten Prüflücken, zurückgezogenen Freigabezuständen und korrigierten Lesungen wie in den erzeugten Daten.[^16]

Eine Transformationsumgebung derselben Gruppe macht den entsprechenden Punkt für Mappings. Ein Output kann seinem Mapping entsprechen und schemavalide sein und die Quelle dennoch unzureichend repräsentieren, und ein Fehler in der Umsetzung eines angemessenen Mappings wird in der Transformation korrigiert und nicht im Mapping, sodass das implementierte Ergebnis erlaubt, Konformität getrennt von Angemessenheit zu prüfen.[^17]

## Evaluation und Audit

Die vierte Gruppe macht den generativen Prozess selbst zum Untersuchungsgegenstand und umfasst Modellvergleich, Analyse von Abweichungen, Bewertung von Outputs und die Prüfung von Pipelines.[^18] Die dokumentierte Praxis liefert eine Instanz dieser reflexiven Wendung auf Methodenebene, denn die Rücknahme agentenvergebener Freigabezustände korrigierte ein Projekt und stützte zugleich die allgemeine Regel, dass Agents Evidenz zusammentragen und vorläufige Einschätzungen festhalten dürfen, ohne selbstständig einen autorisierten Status zu vergeben.[^12] Eine zweite Beobachtung, qualitative Verschlechterung in langen Implementierungssitzungen, änderte auf Projektebene Sitzungslänge, Kontextauffrischung und Rückgriff auf die gepflegten Dokumente und bleibt Kandidat für eine allgemeine Regel, denn die Verallgemeinerung hängt von der Evidenz, von der Wiederkehr über Fälle hinweg und von den Folgen der Regel ab.[^19]

## Was der Vergleich zeigt

Die Fälle beginnen aus verschiedenen Projektzuständen und stellen verschiedene Funktionen der Implementation in den Vordergrund, und jeder erhält ein rekonstruierbares Verhältnis von gepflegtem Projektwissen, referenziertem Forschungsdatenstand, entstandenem Artefakt, Befunden aus dessen Prüfung und verantwortlichem Urteil, sodass die Methode weder eine einzige Projektchronologie noch eine Artefaktform vorschreibt.[^20] Das Korpus umspannt ein Nachlasskorpus mit vorhandenen kodierten Metadaten, einen gestuften Produktionsprozess mit gelieferten Referenzen, ein in Entwicklung befindliches Datenmodell mit Erfassungspraxis, eine begrenzte Antragsprobe, ein bestehendes Korrespondenzkorpus, heterogene nutzerseitig gelieferte Dokumentbilder und Textquellen mit einem entstehenden Kodierungs-Mapping, mit gebundenen Zwecken von der experimentellen Verarbeitungsstrecke bis zum abgenommenen Demonstrator und zur Forschungsvorschau. Diese Variation stützt Praktikabilität und Reichweite der Methode innerhalb der Praxis, aus der sie konsolidiert wurde, und sie belegt keine kausale Wirkung, keine vergleichende Überlegenheit, keine unabhängige Übertragbarkeit und keine vollständige Typologie.[^21] Ein Fall zeigt, wie eine gebundene Abnahme aussieht, wenn sie sauber formuliert ist, denn ein Demonstrator aus der Antragsphase wurde für die Prüfung und Kommunikation eines Förderantrags abgenommen, während korpusweite philologische Angemessenheit und Produktionsreife außerhalb des abgenommenen Zwecks blieben.[^22]

## Gaps
- Projekte, deren Bezeichnung einen Personennamen enthält, werden hier beschreibend benannt, was der Namensregel des Projekts folgt und das Kapitel an Identifizierbarkeit kostet. Ob das Buch diese Projekte benennt, ist eine Operator-Entscheidung.
- Die Gliederung nennt weitere Fälle, darunter Semantic Markdown, Projektvokabulare, Bias-Evaluation und eigene Audit-Oberflächen, die die destillierten Quellen nicht einzeln beschreiben. Sie setzen voraus, dass die betreffende Projektdokumentation als Quelle aufgenommen oder die Fallabschnitte des Papers feiner destilliert werden.
- Das Vergleichsraster der Gliederung verlangt pro Fall Projektkontext, Daten- und Quellenstruktur, Wissensrepräsentationen, agentischen Workflow, Dokumentarchitektur, Prüfverfahren, Artefakttyp, Fehlermodi und Randbedingungen. Die Quellen tragen diese Elemente über die Fälle hinweg ungleich, weshalb dieses Kapitel nach analytischen Problemen vergleicht und nicht Fall für Fall.
- Die Lehrfälle gehören in Kapitel 20 und ruhen auf Material der parallelen Schreiblane.

[^1]: Grounded in [[30_assertions/the-cases-are-reconstructions-under-a-common-analytical-structure]].
[^2]: Grounded in [[30_assertions/four-analytical-dimensions-organise-the-comparison]].
[^3]: Grounded in [[30_assertions/an-artefact-alone-does-not-witness-its-own-history]].
[^4]: Grounded in [[30_assertions/formal-modelling-does-not-determine-the-operational-form]].
[^5]: Grounded in [[30_assertions/interface-findings-concern-the-claims-a-representation-implies]].
[^6]: Grounded in [[30_assertions/early-interfaces-make-a-model-discussable-through-operations]].
[^7]: Grounded in [[30_assertions/implementation-can-participate-in-the-formation-of-a-model]].
[^8]: Grounded in [[30_assertions/a-finding-is-attributed-before-it-is-written-back]].
[^9]: Grounded in [[30_assertions/interaction-exposes-unwarranted-precision]].
[^10]: Grounded in [[30_assertions/the-cases-are-reconstructions-under-a-common-analytical-structure]].
[^11]: Grounded in [[30_assertions/prompt-borne-metadata-can-enter-a-transcription]].
[^12]: Grounded in [[30_assertions/inspection-is-separated-from-the-authority-to-record]].
[^13]: Grounded in [[30_assertions/a-reproducible-metric-does-not-validate-its-own-specification]].
[^14]: Grounded in [[30_assertions/distillation-preserved-uncertainty-and-negative-findings]].
[^15]: Grounded in [[30_assertions/a-public-deployment-is-the-latest-state-of-a-development-history]].
[^16]: Grounded in [[30_assertions/data-production-becomes-accountable-through-a-reconstructable-relation]].
[^17]: Grounded in [[30_assertions/conformity-to-a-mapping-is-examined-separately-from-its-adequacy]].
[^18]: Posit: die vierte analytische Gruppe ist in der Gliederung angekündigt und in den destillierten Quellen nur über Befunde zur Organisation agentischer Arbeit vertreten, weshalb sie hier als Ort im Argument geführt wird und nicht als Menge beschriebener Fälle. Open evidence question: welche dokumentierten Artefakte des Korpus den generativen Prozess selbst zum Gegenstand haben.
[^19]: Grounded in [[30_assertions/project-level-and-method-level-write-back-differ]].
[^20]: Grounded in [[30_assertions/the-cases-share-a-relation-and-not-a-chronology]].
[^21]: Grounded in [[30_assertions/the-documented-corpus-spans-conditions-and-purposes]].
[^22]: Grounded in [[30_assertions/purpose-specific-acceptance-bounds-the-claim]].
