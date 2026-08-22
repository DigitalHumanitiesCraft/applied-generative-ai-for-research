---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-file-collection-is-not-a-knowledge-base]]", "[[30_assertions/a-knowledge-base-is-purpose-bound]]", "[[30_assertions/a-knowledge-document-is-bounded-structured-and-revisable]]", "[[30_assertions/a-knowledge-document-is-materialised-context-compression]]", "[[30_assertions/a-knowledge-document-is-transferable-compact-and-retrievable]]", "[[30_assertions/atomisation-and-consolidation-run-in-opposite-directions]]", "[[30_assertions/context-quality-has-four-criteria]]", "[[30_assertions/distillation-abstracts-a-principle-from-a-case]]", "[[30_assertions/filing-information-is-modelling-work]]", "[[30_assertions/five-transformations-convert-material-into-units]]", "[[30_assertions/four-artefact-kinds-carry-different-duties]]", "[[30_assertions/four-design-principles-guide-the-transformations]]", "[[30_assertions/governance-and-curation-keep-a-holding-usable]]", "[[30_assertions/instruction-files-are-context-not-enforcement]]", "[[30_assertions/instruction-files-externalise-stable-rules]]", "[[30_assertions/knowledge-acquisition-has-two-sources]]", "[[30_assertions/knowledge-engineering-makes-knowledge-explicit]]", "[[30_assertions/markdown-exposes-structure-without-guaranteeing-content]]", "[[30_assertions/provenance-has-a-standard-form-and-a-research-demand]]", "[[30_assertions/the-document-is-the-concept-and-markdown-a-serialization]]", "[[30_assertions/the-five-part-systematics-is-an-own-coinage]]", "[[30_assertions/the-formalisation-target-has-shifted]]", "[[30_assertions/the-gap-is-between-possessed-and-available-knowledge]]", "[[30_assertions/the-granularity-conflict-between-readers-is-unresolved]]", "[[30_assertions/the-knowledge-model-bounds-the-output]]", "[[30_assertions/the-knowledge-system-is-a-production-system]]", "[[30_assertions/the-structure-of-a-holding-is-meaning-bearing]]", "[[30_assertions/the-transformations-are-anchored-in-older-disciplines]]", "[[30_assertions/three-traditions-feed-the-practice]]"]
posits: 1
lang: de
part: "II. Vom Prompting zum grundierten Wissen"
chapter: 6
title: "Knowledge Engineering für generative Forschung"
topic: "[[Grounded-Knowledge]]"
feeding-sources: ["script chapters 3 to 5", "paper (Project Knowledge Base)", "Vault als materialisiertes Wissensmodell"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Knowledge Engineering für generative Forschung

## Die vorgelagerte Frage

Context Engineering entscheidet, was in einer Interaktion verfügbar ist. Knowledge Engineering beantwortet die frühere und dauerhaftere Frage, wie Projektwissen repräsentiert, gepflegt, verknüpft und über Interaktionen hinweg wiederverwendbar gemacht wird, und macht Begriffe, Regeln, Entscheidungen, Einschränkungen und Unsicherheiten so sichtbar, dass sie gelesen, kritisiert und fortgeschrieben werden können. Sein Fokus verschiebt sich von Dateien zu gepflegtem Wissen, sodass sein Gegenstand Erhebung, Strukturierung, Kuration, Provenienz, Revision und Governance umfasst.[^1]

Am Anfang steht eine Lücke. Expert:innen stützen sich auf stillschweigende Unterscheidungen, erinnerte Entscheidungen, lokale Dateistrukturen, disziplinäre Konventionen und Erfahrung, die niemand repräsentiert hat, ein Modell kann nicht verwenden, was nur im Gedächtnis einer Person liegt, und ein Agent kann Konventionen nicht rekonstruieren, die nie aufgeschrieben wurden. Die Frage ist deshalb, ob das relevante Wissen in einer nutzbaren und revidierbaren Form externalisiert wurde.[^2]

Die Dateien zu haben schließt diese Lücke nicht. Wissen in einem Projekt liegt verteilt in Richtlinien, Korrespondenz, Beispielen und der Erfahrung Einzelner, und wer lange dabei ist, ergänzt die fehlenden Zusammenhänge, ohne es zu bemerken. Ein Agent kann alles durchsuchen und dennoch eine alte Regel mit einer neuen mischen oder aus einem einzelnen Beispiel eine Konvention machen, weil vorhandene lokale Ordnung noch kein systemweit nutzbarer Bestand ist.[^3] Der Fehler ist genau zu benennen, weil er wie ein Retrieval-Problem aussieht und ein Repräsentationsproblem ist.

## Woher das Wissen kommt

Zwei Quellen speisen einen Bestand. Vorhandene Dokumente und Daten werden aufbereitet und in maschinenlesbare und destillierte Formen überführt, und Wissen, das in keinem Dokument steht, wird über Dokumentenanalyse, Interviews, Workshops, Beobachtung von Arbeitsabläufen, Fehleranalyse und gemeinsame Modellierung gehoben und in dieselbe strukturierte Form gebracht. Der implizite Teil umfasst die Gründe früherer Entscheidungen, bekannte Ausnahmen, Erwartungen an das Zielartefakt, Akzeptanzkriterien und praktische Erfahrung mit bestimmten Quellentypen, und eine seit Jahren praktizierte Regel kann in keiner Richtlinie stehen, bis ein Interview sie zutage fördert.[^4]

Verändert hat sich gegenüber der klassischen Lesart des Begriffs das Formalisierungsziel. Knowledge Engineering stammt aus der Expertensystem-Tradition, und strukturierte natürliche Sprache mit leichtem Metadaten-Anteil genügt heute dort, wo einst Logik und Ontologie verlangt waren, weil das Sprachmodell das Sprachverstehen beisteuert, das eine formale Repräsentation zuvor kodieren musste.[^5] Die älteren Traditionen speisen die Praxis weiterhin. Wissensmodellierung identifiziert die Konzepte einer Domäne und macht sie abfragbar, Personal Information Management untersucht, wie Menschen Information über Formate und Orte hinweg erwerben, organisieren, pflegen, wiederfinden, nutzen und teilen, mit Fragmentierung als Kernproblem, und Projektmanagement steuert Verfahren für Initiierung, Planung, Durchführung, Überwachung und Abschluss bei. Eine gepflegte Umgebung hält deshalb Begriffsdefinitionen, Quellenverweise, Anforderungen, Entscheidungen, Prozessbeschreibungen, Instruktionen, offene Fragen und Bewertungskriterien zugleich.[^6]

Der Bestand bleibt zweckgebunden. Er führt den Teil des Wissens, den bestimmte Formen von Arbeit, Entscheidung und Prüfung verlangen, und Vollständigkeit ist nicht sein Kriterium.[^7] Das lässt sich leichter durchhalten, wenn der Zweck benannt ist, denn das System dient der Ableitung von Zielartefakten und nicht der Ablage. Kuratierte, verdichtete Dokumente sind die Eingabe des Schritts, der ein Konzept, einen Antrag, eine Spezifikation oder ein Datenmodell erzeugt, und die User Story bildet die Brücke zwischen beiden Tätigkeiten, indem sie eine Anforderung in eine Form bringt, die ein Mensch versteht und ein Agent als Kontext verwenden kann. Anforderungen selbst entstehen aus dem Verhältnis von Daten, Forschungsfragen und wissenschaftlichen Praktiken und nicht aus dem Datenmodell allein.[^8]

## Die Einheit und ihre Eigenschaften

Ein Wissensdokument führt die für einen abgegrenzten Gegenstand relevanten Aussagen in prüfbarer Form zusammen, sodass eine Regel, ihre Ausnahmen und ihre Folgen an einer Stelle gelesen werden können, statt für jede Aufgabe neu gesucht zu werden. Es ist im Gegenstand begrenzt, in der Struktur nachvollziehbar, in seinen Unsicherheiten sichtbar, in seiner Provenienz dokumentiert, revidierbar, dual lesbar für Menschen und Modelle und auf eine Weise kompakt, die die für seinen Zweck nötigen Differenzierungen erhält.[^9]

Das Dokument ist ein Konzept und kein Dateiformat. Plain Text mit leichter Struktur wird hier verwendet, weil er offen, versionierbar, verlinkbar und für Menschen wie Modelle lesbar ist, und das Format legt Struktur mit wenig Auszeichnung frei, ohne über den Inhalt etwas zu garantieren. Es schafft eine geteilte Oberfläche, auf der Menschen und Agents am selben Bestand arbeiten, und es ist reicheren Formaten nicht überlegen, wo Auszeichnungsstandards, strukturierte Datenformate, Datenbanken oder Schemata durch ihre Semantik oder ihre Einschränkungen verlangt sind.[^10]

Was ein solches Dokument schreibenswert macht, ist seine Funktion im Kontext. Es ist materialisierte Context Compression, eine vorab geleistete Verdichtung, die ein Modell nicht jedes Mal neu aus dem Rohmaterial herstellen muss.[^11] Die Eigenschaften folgen aus dieser Funktion. Ein gutes Dokument ist transferierbar, sodass das Wissen auf beim Schreiben unbekannte Situationen anwendbar bleibt, kompakt, sodass nur enthalten ist, was die Anwendung braucht, und abrufbar, sodass Überschriften, Metadaten und Gliederung es rasch wieder aktivierbar machen, und es setzt eine Leserschaft voraus, die den Kontext kennt oder sich erschließen kann.[^12]

Seine Herstellung hat eine Form und einen Abnahmetest. Distillation führt von einem konkreten Fall über die Extraktion von Mustern und ihre Abstraktion zu vom Einzelfall gelösten Prinzipien zu einer Verdichtung in eine speicherbare Form, das Ergebnis gilt unabhängig vom Ausgangsbeispiel, und der Test lautet, ob jemand, der nur das Dokument liest, das Prinzip ohne Rückfragen auf einen neuen Fall anwenden kann.[^13] Als Kontext beurteilt ist ein brauchbares Dokument von mittlerem Umfang statt Stub oder Monolith, trägt Frontmatter, Sektionen und Quellen, erklärt sich selbst ohne andere Dokumente vorauszusetzen und dupliziert nichts, was anderswo liegt.[^14]

## Operationen am Bestand

Ein Bestand verändert sich über eine kleine Menge von Operationen. Wissenstransformationen überführen Information in wiederverwendbare, kontextualisierte Strukturen, und fünf davon tragen das Vorgehen, Kompression oder Destillation, Normalisierung, Anreicherung, Konsolidierung und Atomisierung, jede bestimmt durch Input, Output und die Richtung ihres Informationsflusses.[^15] Zwei von ihnen laufen gegenläufig und dienen demselben Ziel. Atomisierung teilt eine monolithische Mitschrift, in der viele einzeln referenzierbare Konzepte vermischt liegen, in atomare Dokumente auf, während das Ausgangsdokument zu einem Hub wird, der auf sie verweist, Konsolidierung führt mehrere Dokumente mit redundanten Grundlagen zu einem zusammen, in dem die Redundanz getilgt ist, und beide zielen auf die saubere Zuordnung von einem Konzept zu einer Einheit.[^16]

Vier Prinzipien leiten die Operationen. Ein Konzept bewohnt genau ein Dokument, jedes Dokument bleibt für sich verständlich, Informationsdichte wird pro Token maximiert ohne Redundanz zwischen Dokumenten, und Provenienz wird über eine Quellensektion und Frontmatter gesichert. Self-Containedness ist das Prinzip, das über die Verwendbarkeit als Kontext entscheidet, weil der Kontext, den ein Dokument braucht, im Dokument stehen muss und nicht nur in seinen Links.[^17]

Die Operationen sind nicht erfunden. Kompression entspricht dem Referieren, Normalisierung der formalen Beschreibung nach Regelwerk, Anreicherung der Sacherschließung und semantischen Erschließung, Konsolidierung der Information Consolidation mit ihrer Trennung von Gehalt und Form, und Atomisierung dem monographischen Prinzip der Dokumentation sowie einer Zettelkasten-Praxis mit atomaren, fest adressierten, quervernetzten Einheiten.[^18] Provenienz trägt ebenfalls ein Erbe, einen maschinenlesbaren Standard mit Entity, Activity, Agent und einer Ableitungsrelation sowie eine forschungspraktische Forderung in den FAIR-Prinzipien, während der gesamte Vorgang, Wissen in ablegbare Dokumente zu fassen, die Knowledge Codification mit einem Stufenmodell aus Capturing, Packaging und Reusing ist.[^19] Die Fünfer-Systematik selbst ist eine Prägung. Eine kanonische Taxonomie von Dokumenttransformationen existiert in keiner der beteiligten Disziplinen, und die Systematik ist als facettierte Klassifikation über zwei Achsen hergeleitet, an den Einheitsgrenzen durch Zerlegen oder Zusammenführen und an der Einheit selbst durch Reduzieren, Erweitern oder Umordnen der Form.[^20]

## Was die Struktur entscheidet

Die Struktur eines Bestandes trägt Bedeutung. Ein gesetzter Link, ein gewählter Tag und die Aufteilung eines Dokuments in kleinere Einheiten entscheiden, wie das Wissen später von einer menschlichen Leserin und von einem Modell interpretiert werden kann, weil sie festlegen, welche Zusammenhänge sichtbar sind, welche Konzepte als eigenständig gelten und wie sich das Netz beim selektiven Laden verhält.[^21] Ablegen ist deshalb Modellieren, und strukturelle Pflege formt ein Modell des eigenen Wissens, statt einen Ordner aufzuräumen.[^22] Was dieses Modell taugt, begrenzt, was sich daraus erzeugen lässt.[^23]

Zwei Dinge folgen für die Praxis. Das erste ist, dass Pflege inhaltliche Arbeit ist. Ein Bestand verliert ohne sie an Nutzbarkeit, Dokumente veralten, Begriffe werden uneinheitlich und parallele Fassungen widersprechen einander, sodass Governance die Regeln setzt und Kuration sie anwendet, strukturell auf Namen, Metadaten, Links, Dokumenttypen, Versionen und Dubletten und inhaltlich auf Widersprüche, veraltete Regeln, fehlende Einschränkungen, unangemessene Verdichtungen und die Revision von Anforderungen. Ein Agent kann Probleme lokalisieren und Vorschläge erzeugen, und folgenreiche Änderungen müssen geprüft und verantwortet werden.[^24]

Das zweite ist, dass vier Artefaktarten verschiedene Pflichten tragen und einander nicht aufsaugen sollten. Ein Wissensdokument beschreibt, was über einen Gegenstand bekannt ist, eine Instruktionsdatei regelt die wiederkehrende Arbeit, ein Skill operationalisiert ein wiederverwendbares Verfahren, und ein Prompt formuliert die aktuelle Aufgabe.[^25] Instruktionsdateien rechtfertigen ihren Platz dadurch, dass sie externalisieren, was sonst neu getippt würde, mit dauerhafter personengebundener Policy auf der einen und Projektfakten auf der anderen Ebene, und die Aufnahmesignale lauten, dass der Agent einen Fehler wiederholt, dass ein Review etwas findet, das er hätte wissen müssen, dass dieselbe Korrektur erneut getippt wird oder dass ein neues Teammitglied denselben Kontext brauchte.[^26] Sie sind Kontext und keine Durchsetzung, und Verhaltensanleitung ist etwas anderes als Berechtigungen und Hooks, die eine Grenze unabhängig von der Befolgung halten können.[^27]

Eine Frage bleibt in den Quellen offen. Ein für menschliches Lesen gebautes Modell und ein für Maschinenkontext gebautes können unterschiedliche Granularität verlangen, der Konflikt zwischen kompakter Maschinenlesbarkeit und ausführlicher menschlicher Nachvollziehbarkeit ist ungeklärt, und woran sich die Qualität eines Wissensmodells überhaupt messen ließe, ist es ebenso.[^28]

## Lücken

Zwei Themen, die die Gliederung diesem Kapitel zuweist, reichen über die Quellen dieser Arbeitslinie hinaus.[^29]
- Formale und halbformale Repräsentation, kontrollierte Vokabulare, Schemata und Ontologien, erscheinen hier nur als Nachbartradition der Wissensmodellierung und als Hinweis, dass reichere Formate dort vorzuziehen bleiben, wo ihre Semantik verlangt ist. Wann ein Projekt zu einer formalen Repräsentation statt zu strukturierter Prosa greifen sollte, steht in diesen Quellen nirgends.
- Die Unterscheidung zwischen Wissen, Annahmen, Regeln, Anforderungen und Entscheidungen tragen die Quellen über die Liste dessen, was eine gepflegte Umgebung hält, und nicht über eine Typologie mit Kriterien. Die Dokumenttypologie der anderen Manuskriptlinie ist der Ort dieser Unterscheidung, und dieses Kapitel verweist dafür auf Kapitel 14.

[^1]: Grounded in [[30_assertions/knowledge-engineering-makes-knowledge-explicit]].
[^2]: Grounded in [[30_assertions/the-gap-is-between-possessed-and-available-knowledge]].
[^3]: Grounded in [[30_assertions/a-file-collection-is-not-a-knowledge-base]].
[^4]: Grounded in [[30_assertions/knowledge-acquisition-has-two-sources]].
[^5]: Grounded in [[30_assertions/the-formalisation-target-has-shifted]].
[^6]: Grounded in [[30_assertions/three-traditions-feed-the-practice]].
[^7]: Grounded in [[30_assertions/a-knowledge-base-is-purpose-bound]].
[^8]: Grounded in [[30_assertions/the-knowledge-system-is-a-production-system]].
[^9]: Grounded in [[30_assertions/a-knowledge-document-is-bounded-structured-and-revisable]].
[^10]: Grounded in [[30_assertions/the-document-is-the-concept-and-markdown-a-serialization]], [[30_assertions/markdown-exposes-structure-without-guaranteeing-content]].
[^11]: Grounded in [[30_assertions/a-knowledge-document-is-materialised-context-compression]].
[^12]: Grounded in [[30_assertions/a-knowledge-document-is-transferable-compact-and-retrievable]].
[^13]: Grounded in [[30_assertions/distillation-abstracts-a-principle-from-a-case]].
[^14]: Grounded in [[30_assertions/context-quality-has-four-criteria]].
[^15]: Grounded in [[30_assertions/five-transformations-convert-material-into-units]].
[^16]: Grounded in [[30_assertions/atomisation-and-consolidation-run-in-opposite-directions]].
[^17]: Grounded in [[30_assertions/four-design-principles-guide-the-transformations]].
[^18]: Grounded in [[30_assertions/the-transformations-are-anchored-in-older-disciplines]].
[^19]: Grounded in [[30_assertions/provenance-has-a-standard-form-and-a-research-demand]].
[^20]: Grounded in [[30_assertions/the-five-part-systematics-is-an-own-coinage]].
[^21]: Grounded in [[30_assertions/the-structure-of-a-holding-is-meaning-bearing]].
[^22]: Grounded in [[30_assertions/filing-information-is-modelling-work]].
[^23]: Grounded in [[30_assertions/the-knowledge-model-bounds-the-output]].
[^24]: Grounded in [[30_assertions/governance-and-curation-keep-a-holding-usable]].
[^25]: Grounded in [[30_assertions/four-artefact-kinds-carry-different-duties]].
[^26]: Grounded in [[30_assertions/instruction-files-externalise-stable-rules]].
[^27]: Grounded in [[30_assertions/instruction-files-are-context-not-enforcement]].
[^28]: Grounded in [[30_assertions/the-granularity-conflict-between-readers-is-unresolved]].
[^29]: Posit: die Lückenliste hält fest, wo dieses Kapitel hinter der Gliederung zurückbleibt. Open evidence question: ob sich ein Kriterium für die Wahl einer formalen Repräsentation gegenüber strukturierter Prosa aus den vergleichenden Fällen in Teil V gewinnen lässt.
