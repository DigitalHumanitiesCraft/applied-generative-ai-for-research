---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-knowledge-document-is-bounded-structured-and-revisable]]", "[[30_assertions/a-knowledge-document-is-materialised-context-compression]]", "[[30_assertions/a-knowledge-document-is-transferable-compact-and-retrievable]]", "[[30_assertions/an-external-memory-is-shared-between-human-and-agent]]", "[[30_assertions/atomisation-and-consolidation-run-in-opposite-directions]]", "[[30_assertions/context-quality-has-four-criteria]]", "[[30_assertions/distillation-abstracts-a-principle-from-a-case]]", "[[30_assertions/filing-information-is-modelling-work]]", "[[30_assertions/five-transformations-convert-material-into-units]]", "[[30_assertions/four-artefact-kinds-carry-different-duties]]", "[[30_assertions/four-design-principles-guide-the-transformations]]", "[[30_assertions/governance-and-curation-keep-a-holding-usable]]", "[[30_assertions/instruction-files-are-context-not-enforcement]]", "[[30_assertions/knowledge-engineering-makes-knowledge-explicit]]", "[[30_assertions/persistent-knowledge-keeps-change-visible]]", "[[30_assertions/provenance-has-a-standard-form-and-a-research-demand]]", "[[30_assertions/the-granularity-conflict-between-readers-is-unresolved]]", "[[30_assertions/the-knowledge-model-bounds-the-output]]", "[[30_assertions/the-structure-of-a-holding-is-meaning-bearing]]", "[[30_assertions/three-levels-separate-holding-task-and-window]]"]
posits: 6
lang: de
part: "II. Vom Prompting zum grundierten Wissen"
chapter: 7
title: "Der Grounded Vault"
topic: "[[Grounded-Knowledge]]"
feeding-sources: ["script chapters 3 to 5", "paper (Project Knowledge Base)", "Vault als materialisiertes Wissensmodell"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Der Grounded Vault

## Was der Begriff bezeichnet

Ein Grounded Vault ist eine persistente Wissensumgebung, die Forschende und computationelle Agents teilen und in der Quellen, strukturierte Daten, Projektwissen, Prozessgedächtnis, Handlungsanweisungen und Prüfmaterial in einer Form gehalten werden, die nachvollzogen, kritisiert und revidiert werden kann. Bestimmt wird er durch die Organisation und Governance dessen, was er hält, und nicht durch eine Anwendung, sodass ein Repository, ein lokales Dateisystem, ein Plain-Text-Notizsystem oder eine vergleichbare Infrastruktur ihn tragen kann.[^0]

Die Lesart, die den Begriff über ein Synonym für Ordner hinaushebt, stammt aus den Quellen. Ein Bestand offener Textdateien ist ein materialisiertes semantisches Netz, in dem Links, Tags und Hierarchien selbst Bedeutung tragen, weil ein gesetzter Link, ein gewählter Tag und die Aufteilung eines Dokuments in kleinere Einheiten darüber entscheiden, wie das Wissen später von einer menschlichen Leserin und von einem Modell interpretiert werden kann, und dabei festlegen, welche Zusammenhänge sichtbar sind, welche Konzepte als eigenständig gelten und wie sich das Netz beim selektiven Laden verhält.[^1] Ablegen ist deshalb Modellieren, und strukturelle Pflege formt ein Modell des Projektwissens, statt ein Verzeichnis aufzuräumen.[^2] Was dieses Modell taugt, begrenzt, was sich daraus erzeugen lässt, und deshalb wird die Umgebung hier als Gestaltungsgegenstand behandelt.[^3]

Die Paarung mit einem Agenten folgt aus einer Eigenschaft der in Teil I beschriebenen Systeme. Ein Context Window ist ein begrenztes, flüchtiges Arbeitsgedächtnis, während ein Ordner offener Textdateien der Langzeitspeicher ist, und weil die Dateien offen sind, liest und schreibt der Agent genau das, was auch ein Mensch liest und schreibt.[^4] Ein solches externes Gedächtnis organisiert individuelles und institutionelles Wissen, steuert operative Arbeit und repräsentiert Wissensstrukturen zugleich.

## Die Bedingungen

Für eine solche Umgebung werden üblicherweise sieben Bedingungen genannt, und die Quellen dieses Buches stützen sie unterschiedlich gut. Zwei gelten ohne weitere Begründung. Die Umgebung muss inspizierbar sein, damit Menschen lesen, kritisieren und revidieren können, was gehalten wird, und revidierbar, damit neue Erkenntnisse die gepflegte Schicht verändern, statt in lokalen Ausgaben zu bleiben. Beides folgt aus der Bestimmung von Knowledge Engineering als Aufbau und Pflege expliziten, inspizierbaren und revidierbaren Projektwissens, dessen Gegenstand Erhebung, Strukturierung, Kuration, Provenienz, Revision und Governance umfasst.[^5]

Agentenbedienbarkeit folgt aus dem geteilten externen Gedächtnis. Der Agent arbeitet an denselben Dateien wie die Person, sodass die Eigenschaft eine Folge des Formats ist und kein Zusatz.[^4] Die Schichtung folgt aus den drei Ebenen, die einen persistenten Bestand von einem aufgabenspezifischen Working Context und vom technischen Fenster trennen, in dem dieser Kontext verarbeitet wird, samt der weiteren Trennung von vier Artefaktarten, einem Wissensdokument, das einen Gegenstand beschreibt, einer Instruktionsdatei, die wiederkehrende Arbeit regelt, einem Skill, der ein Verfahren operationalisiert, und einem Prompt, der die aktuelle Aufgabe formuliert.[^6]

Die Versionierung trägt die Beobachtung, dass persistentes Projektwissen Menschen und Systeme auf denselben dokumentierten Stand verweisen lässt, sodass Aussagen kritisiert, aktualisiert und an Evidenz gebunden werden können, während Änderungen sichtbar bleiben.[^7] Wichtig ist hier die Sichtbarkeit der Revision und nicht die Speicherung von Historie.

Die beiden verbleibenden Bedingungen verlangen mehr Sorgfalt. Governance erscheint in den Quellen als Forderung und nicht als Mechanismus. Sie setzt die Regeln für Aufbau, Änderung und Nutzung, Kuration wendet sie strukturell und inhaltlich an, ein Agent kann Probleme lokalisieren und Vorschläge erzeugen, und folgenreiche Änderungen müssen geprüft und verantwortet werden.[^8] Was fehlt, ist die Durchsetzung. Eine Instruktionsdatei ist Kontext und keine Garantie, und Verhaltensanleitung ist etwas anderes als Berechtigungen und Hooks, die eine Grenze unabhängig von der Befolgung halten können.[^9] Ein Vault ist in dem Maß governed, in dem er beides trennt, und die Quellen dieser Arbeitslinie formulieren die Forderung, ohne eine Architektur zu beschreiben, die sie erfüllt.[^10]

Die Quellengebundenheit ist die Bedingung, nach der die Quellen greifen und die sie nicht liefern. Provenienz verlangen sie alle, und sie trägt ein echtes Erbe, einen maschinenlesbaren Standard mit Entity, Activity, Agent und einer Ableitungsrelation sowie eine forschungspraktische Forderung in den FAIR-Prinzipien, während der Vorgang, Wissen in ablegbare Dokumente zu fassen, die Knowledge Codification mit einem Stufenmodell aus Capturing, Packaging und Reusing ist.[^11] Innerhalb eines Dokuments erfüllen eine Quellensektion und Frontmatter mit Anlage, Quelle und Status die Forderung.[^12] Was keine der Quellen beschreibt, ist eine Kette, die eine einzelne Aussage an die Stelle bindet, die sie stützt. Diese Kette ist die eigene Erweiterung dieses Buches, und sie ist das, was der Vault hinter diesem Manuskript der beschriebenen Praxis hinzufügt.[^13]

## Die Einheit und ihre Herstellung

Die Umgebung besteht aus Wissensdokumenten. Jedes führt die für einen abgegrenzten Gegenstand relevanten Aussagen in prüfbarer Form zusammen, begrenzt im Gegenstand, nachvollziehbar in der Struktur, sichtbar in seinen Unsicherheiten, dokumentiert in seiner Provenienz, revidierbar, dual lesbar und auf eine Weise kompakt, die die für seinen Zweck nötigen Differenzierungen erhält.[^14] Pflegenswert macht es seine Funktion im Kontext, denn es ist eine vorab geleistete Verdichtung, die ein Modell nicht jedes Mal neu aus dem Rohmaterial herstellen muss.[^15]

Diese Funktion erwirbt ein Dokument dadurch, dass es transferierbar, kompakt und abrufbar ist, sodass das Wissen auf beim Schreiben unbekannte Situationen anwendbar bleibt, nur enthalten ist, was die Anwendung braucht, und Überschriften, Metadaten und Gliederung es rasch wieder aktivierbar machen.[^16] Der Weg zu einem solchen Dokument führt von einem konkreten Fall über die Extraktion von Mustern und ihre Abstraktion zu vom Einzelfall gelösten Prinzipien zu einer Verdichtung in eine speicherbare Form, und der Abnahmetest lautet, ob jemand, der nur das Dokument liest, das Prinzip ohne Rückfragen auf einen neuen Fall anwenden kann.[^17]

Die Umgebung verändert sich über eine kleine Menge von Operationen. Fünf Transformationen überführen Material in Einheiten, Kompression oder Destillation, Normalisierung, Anreicherung, Konsolidierung und Atomisierung.[^18] Zwei davon sind gegenläufig und dienen demselben Ziel, Atomisierung teilt eine monolithische Mitschrift in atomare Dokumente auf, während das Ausgangsdokument zum Hub wird, Konsolidierung führt Dokumente mit redundanten Grundlagen zu einem zusammen, in dem die Redundanz getilgt ist, und beide zielen auf ein Konzept in einer Einheit.[^19] Vier Prinzipien leiten sie, ein Konzept pro Dokument, Self-Containedness, Informationsdichte und gesicherte Provenienz, und Self-Containedness entscheidet über die Verwendbarkeit als Kontext.[^20] Als Kontext beurteilt ist ein brauchbares Dokument von mittlerem Umfang, trägt Frontmatter, Sektionen und Quellen, erklärt sich selbst und dupliziert nichts, was anderswo liegt.[^21]

## Kuratiertes und generiertes Wissen

Zwei Arten von Inhalt liegen in einer solchen Umgebung und dürfen nicht gleich behandelt werden. Kuratierte Dokumente bleiben in wissenschaftlicher Verantwortung, auch wo ein Modell beim Entwurf mitgewirkt hat, und generierte Dokumente werden von einem benannten Prozess aus Daten erzeugt und beim nächsten Lauf überschrieben. Die Unterscheidung entscheidet, ob eine Bearbeitung ein Beitrag oder ein Verlust ist, und die Quellen dieser Arbeitslinie ziehen sie nicht.[^22]

Was die Quellen liefern, ist das Pflegeregime, das beide Arten nutzbar hält. Ein Bestand verliert ohne Kuration an Nutzbarkeit, Dokumente veralten, Begriffe werden uneinheitlich und parallele Fassungen widersprechen einander, sodass Governance die Regeln setzt und Kuration sie strukturell auf Namen, Metadaten, Links, Dokumenttypen, Versionen und Dubletten und inhaltlich auf Widersprüche, veraltete Regeln, fehlende Einschränkungen, unangemessene Verdichtungen und die Revision von Anforderungen anwendet.[^8]

Eine Frage bleibt über all dem offen. Ein für menschliches Lesen gebautes Modell und ein für Maschinenkontext gebautes können unterschiedliche Granularität verlangen, der Konflikt zwischen kompakter Maschinenlesbarkeit und ausführlicher menschlicher Nachvollziehbarkeit ist in den Quellen ungeklärt, und woran sich die Qualität eines Wissensmodells überhaupt messen ließe, ist es ebenso.[^23] Ein Buch, das den Bau einer solchen Umgebung empfiehlt, muss sagen, dass die Empfehlung auf Praxis ruht und nicht auf einer Messung.[^24]

## Lücken

Drei Punkte der Gliederung sind nur teilweise abgedeckt.[^25]
- Die Unterscheidung zwischen kuratiertem und deterministisch erzeugtem Wissen wird hier benannt und ist in nichts verankert. Keine Quelle dieser Arbeitslinie zieht sie, und die Dokumenttypologie der anderen Manuskriptlinie ist ihr Ort, sodass Kapitel 14 sie trägt.
- Die Liste dessen, was ein Grounded Vault enthalten kann, von Schemata und Standards über Verifikationskonzepte bis zu publizierten Artefakten, steht in der Gliederung und erscheint in diesen Quellen nur als lockerere Aufzählung dessen, was eine gepflegte Umgebung hält. Das Destillat des Promptotyping-Papers ist der Ort für die Verankerung der vollständigen Liste.
- Die sieben Bedingungen sind hier einzeln verankert, und die Zahl sieben ist die Zählung der Gliederung. Ob die Menge vollständig ist, kann keine Quelle dieser Arbeitslinie beantworten.

[^0]: Posit: der Begriff Grounded Vault und die hier gegebene Definition sind eigene Setzungen dieses Buches, zusammengesetzt aus Eigenschaften, die seine Quellen einzeln beschreiben. Open evidence question: ob eine Umgebung, die der Definition genügt, von einer Leserin als solche erkannt wird, die nur die Definition und eine umgesetzte Instanz vor sich hat.
[^1]: Grounded in [[30_assertions/the-structure-of-a-holding-is-meaning-bearing]].
[^2]: Grounded in [[30_assertions/filing-information-is-modelling-work]].
[^3]: Grounded in [[30_assertions/the-knowledge-model-bounds-the-output]].
[^4]: Grounded in [[30_assertions/an-external-memory-is-shared-between-human-and-agent]].
[^5]: Grounded in [[30_assertions/knowledge-engineering-makes-knowledge-explicit]].
[^6]: Grounded in [[30_assertions/three-levels-separate-holding-task-and-window]], [[30_assertions/four-artefact-kinds-carry-different-duties]].
[^7]: Grounded in [[30_assertions/persistent-knowledge-keeps-change-visible]].
[^8]: Grounded in [[30_assertions/governance-and-curation-keep-a-holding-usable]].
[^9]: Grounded in [[30_assertions/instruction-files-are-context-not-enforcement]].
[^10]: Posit: die Governance-Bedingung nur dort als erfüllt zu lesen, wo Anleitung und Durchsetzung getrennt sind, ist ein eigenes Kriterium dieses Buches, und keine Quelle formuliert es. Open evidence question: ein Vergleich von Projekten, die beides trennen, mit solchen, die es nicht tun, gemessen an unautorisierten Änderungen an einem gepflegten Bestand.
[^11]: Grounded in [[30_assertions/provenance-has-a-standard-form-and-a-research-demand]].
[^12]: Grounded in [[30_assertions/four-design-principles-guide-the-transformations]].
[^13]: Posit: die Ankerkette, die eine einzelne Aussage an eine stützende Quellenstelle bindet, ist die Erweiterung dieses Buches gegenüber der Praxis seiner Quellen, und sie ist der Mechanismus, mit dem dieses Manuskript selbst geschrieben wird. Open evidence question: ob die Kette den Kontakt mit einem Projekt übersteht, dessen Quellen nicht vollständig gespeichert werden dürfen und in dem ein Zitat an die Stelle einer Blockreferenz tritt.
[^14]: Grounded in [[30_assertions/a-knowledge-document-is-bounded-structured-and-revisable]].
[^15]: Grounded in [[30_assertions/a-knowledge-document-is-materialised-context-compression]].
[^16]: Grounded in [[30_assertions/a-knowledge-document-is-transferable-compact-and-retrievable]].
[^17]: Grounded in [[30_assertions/distillation-abstracts-a-principle-from-a-case]].
[^18]: Grounded in [[30_assertions/five-transformations-convert-material-into-units]].
[^19]: Grounded in [[30_assertions/atomisation-and-consolidation-run-in-opposite-directions]].
[^20]: Grounded in [[30_assertions/four-design-principles-guide-the-transformations]].
[^21]: Grounded in [[30_assertions/context-quality-has-four-criteria]].
[^22]: Posit: die Unterscheidung zwischen kuratiertem und deterministisch erzeugtem Inhalt stammt aus der Gliederung und ist in keiner Quelle dieser Arbeitslinie verankert. Open evidence question: ob das Destillat des Promptotyping-Papers sie trägt und mit welchem Kriterium es den Fall eines generierten Dokuments entscheidet, das später von einer Person bearbeitet wurde.
[^23]: Grounded in [[30_assertions/the-granularity-conflict-between-readers-is-unresolved]].
[^24]: Posit: die Empfehlung als auf Praxis und nicht auf Messung ruhend zu benennen folgt aus der offenen Frage, die die Quellen lassen. Open evidence question: ein Maß für die Qualität eines Wissensmodells, das sich auf zwei Bestände anwenden und vergleichen ließe.
[^25]: Posit: die Lückenliste hält fest, wo dieses Kapitel hinter der Gliederung zurückbleibt. Open evidence question: ob die sieben Bedingungen eine vollständige Menge bilden, was nur ein Vergleich mehrerer umgesetzter Umgebungen entscheiden könnte.
