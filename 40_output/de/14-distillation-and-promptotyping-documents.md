---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-governance-document-records-authority-and-permissions]]", "[[30_assertions/a-technology-baseline-carries-a-family-of-artefacts]]", "[[30_assertions/a-wrong-output-is-diagnosed-by-document-type]]", "[[30_assertions/agent-instruction-documents-translate-knowledge-into-imperatives]]", "[[30_assertions/an-outdated-rule-set-is-the-costliest-decay]]", "[[30_assertions/declarative-documents-state-what-the-project-takes-to-be-the-case]]", "[[30_assertions/derived-artefacts-are-not-maintained-knowledge]]", "[[30_assertions/design-knowledge-stays-declarative]]", "[[30_assertions/distillation-is-not-summarisation-or-compression]]", "[[30_assertions/distillation-is-the-documentary-operation-of-context-engineering]]", "[[30_assertions/domain-knowledge-carries-disciplinary-stipulation]]", "[[30_assertions/process-documents-preserve-how-the-understanding-developed]]", "[[30_assertions/the-action-layer-is-injected-and-therefore-kept-thin]]", "[[30_assertions/the-agent-enters-the-knowledge-base-through-its-index]]", "[[30_assertions/the-architecture-document-gives-the-agent-its-module-boundaries]]", "[[30_assertions/the-charter-carries-the-project-identity]]", "[[30_assertions/the-handoff-document-is-a-process-inbox]]", "[[30_assertions/the-index-routes-a-knowledge-base]]", "[[30_assertions/the-integration-document-holds-the-contract-at-the-boundary]]", "[[30_assertions/the-journal-is-a-curated-provenance-index]]", "[[30_assertions/the-knowledge-base-differs-from-the-working-context]]", "[[30_assertions/the-knowledge-base-is-a-set-of-interrelated-documents]]", "[[30_assertions/the-material-document-carries-epistemic-responsibility]]", "[[30_assertions/the-method-core-of-the-action-layer-is-portable]]", "[[30_assertions/the-plan-is-the-forward-looking-counterpart-of-the-journal]]", "[[30_assertions/the-report-addresses-an-external-reader]]", "[[30_assertions/the-specification-holds-interlocked-questions-in-one-place]]", "[[30_assertions/the-sufficiency-of-distillation-is-practical]]"]
posits: 0
lang: de
part: "IV. Promptotyping"
chapter: 14
title: "Distillation und Promptotyping Documents"
topic: "[[Promptotyping]]"
feeding-sources: ["paper chapter 2", "script chapter 7", "Promptotyping document templates"]
working-title: true
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Distillation und Promptotyping Documents

## Die Operation

Distillation überführt das in Preparation und Exploration gewonnene Verständnis in die gepflegten Wissensdokumente, aus denen Implementierung und Prüfung hervorgehen, und sie ist die zentrale dokumentarische Operation des Context Engineering innerhalb von Promptotyping.[^1] Was dabei entsteht, repräsentiert das für den aktuellen Zweck nötige Projektwissen und lässt die umfangreicheren Quellen und Forschungsdaten für direkte Prüfung und computationelle Verarbeitung verfügbar.[^1]

Die Operation lässt sich leicht mit Zusammenfassung verwechseln, und die Verwechslung hat praktische Folgen. Die nominelle Kontextkapazität eines Modells besagt nicht, dass alle zugeführte Information zuverlässig genutzt wird, und zusätzliches oder schlecht ausgewähltes Material kann die Nutzung der relevanten Information erschweren, weshalb es der Distillation um eine prüfbare und selektive Repräsentation geht, die diejenigen Unterscheidungen, Bedingungen und Unsicherheiten bewahrt, die eine angemessene Implementierung und Prüfung verlangen.[^2] Weil dasselbe Material anders destilliert werden muss, sobald sich Zweck oder intendiertes Artefakt ändern, ist die Operation eine Form pragmatischer Modellierung und keine feste Reduktion der Quelle.[^2]

Auswahl ist damit konstitutiv. Die dauerhafte Wissensbasis hält das gepflegte Verständnis des Projekts, der Arbeitskontext eines Agents hält das, was ein bestimmter Auftrag braucht, und die Methode behandelt die Entscheidung zwischen beiden als Teil des Context Engineering, statt Anhäufung an deren Stelle treten zu lassen.[^3] Ein Agent kann einen destillierten Bericht zusammen mit aufgabenrelevanten Auszügen aus den Daten erhalten, während prüfbare computationelle Operationen den vollständigen Datenbestand außerhalb des Modellkontexts verarbeiten.[^3]

## Was ein Promptotyping Document ist

Die Dokumente der Wissensbasis sind begrenzte Repräsentationen, aus umfangreicherem Forschungsmaterial destilliert, für menschliche Prüfung und Revision gepflegt und für die Arbeitskontexte von Agents verfügbar.[^4] Aus dieser doppelten Leserschaft folgen sechs Eigenschaften. Ein solches Dokument ist für Fachwissenschaft lesbar und für Agents handlungsleitend, es ist versioniert und revidierbar, es bleibt kompakt genug für eine gesteuerte Kontextarchitektur, und es bleibt auf die Quellen- und Entscheidungsgrundlage des Projekts rückführbar.

Ihre Typen sind organisatorische Heuristiken und keine vorgeschriebene Dateistruktur, sodass Projekte die Funktionen benennen, zusammenlegen und verteilen können, wie ihre Arbeit es verlangt.[^4] Drei Funktionen kehren wieder. Declarative Documents halten fest, was das Projekt derzeit für den Fall hält und was das Artefakt leisten soll.[^5] Process Documents bewahren, wie das Verständnis entstanden ist und wohin die Arbeit geht.[^6] Agent Instruction Documents übersetzen das gepflegte Wissen in Imperative und tragen selbst kein Wissen.[^7]

Die Typen unterscheiden sich nicht im Ton, und eine als begründete Prosa geschriebene Regel kann dennoch ein Action Document sein. Entscheidend ist die Frage, welches Dokument nachzuziehen ist, wenn der Output nicht stimmt. Ein formal falscher Output, ein Stilbruch oder ein ignoriertes Verbot wird im Action Document diagnostiziert; ein inhaltlich falscher Output wird in den Wissensdokumenten diagnostiziert und nicht im Action Layer nachgebessert.[^8]

## Die wiederkehrenden Dokumente

Ein Index erschließt die Wissensbasis, sobald sie mehr als drei Dokumente enthält. Er adressiert eine prüfende Person, einen neu aufgesetzten Coding-Agenten und die projektverantwortliche Person, die nach einer Pause zurückkommt, und er beantwortet, welche Dokumente existieren, welche Frage jedes von ihnen bedient, in welcher Reihenfolge gelesen wird und welche Begriffe konstitutiv sind. Seine einzige Update-Pflicht ist die Konsistenz gegen den realen Ordnerinhalt, denn ein Index, der sie verliert, ist schlechter als keiner, weil er falsche Sicherheit erzeugt.[^9] Die Lesereihenfolge, die er vorgibt, ist der Einstiegsweg jeder Session, vom Index über die offenen Übergabepunkte zum aufgabenrelevanten Dokument, und sie muss auf repo-interne Quellen zeigen, denn ein Repository, dessen Methodenwissen nur in einem externen Vault liegt, ist in einer Session ohne Vault-Zugriff blind.[^10]

Ein Charter-Dokument trägt Identität und Geltungsbereich des Projekts. Es ist der kanonische Bericht darüber, was das Projekt ist, und ein öffentliches README kann daraus ableiten und auf die Wissensbasis zurückverweisen.[^11]

Das Materialdokument trägt die epistemische Verantwortung für die Daten. Es beantwortet, was sie sind, woher sie kommen, wie sie modelliert sind und wo sie aufhören zu tragen, und hält pro Quelle Herkunft, Erfassungslogik, Lizenz, Provenienz und Erfassungszeitraum fest.[^12] Ein Domain-Knowledge-Dokument trägt jede fachliche Setzung, die weder aus dem Material noch aus einer Softwareanforderung folgt, etwa Editionsrichtlinien, ein Kodierungs-Mapping, eine Berechnungslogik oder eine Ontologie, und es trennt die begründende Schicht, die das Warum trägt, vom Regelwerk, das das Wie festlegt.[^13] Der teuerste Verfall der gesamten Wissensbasis liegt hier, in einem Regelwerk, das ein abgelöstes Schema weiter als geltend beschreibt, während das arbeitende Team längst weitergezogen ist, weshalb eine Schemaänderung das Regelwerk im selben Arbeitsgang nachzieht.[^14]

Die Specification führt Anforderungen, narrative Szenarien, Funktionsumfang und Entscheidungen zusammen, weil eine Story eine Anforderung motiviert, ein Feature sie implementiert und eine Entscheidung begründet, warum dieses Feature so gebaut ist, sodass eine Trennung der Schichten eine Änderung in einer Schicht die anderen unbemerkt veralten ließe.[^15] Das Architecture-Dokument trägt die technische Realisierung und gibt dem Agenten die Modulgrenzen, gegen die er baut, denn eine zu vage Beschreibung erzeugt Code, der die intendierten Schichten ignoriert.[^16] Wo mehrere Projekte Artefakte einer Familie bauen, trägt eine Technology Baseline die gemeinsamen Stack-Entscheidungen zentral, und die Architektur einer Instanz hält nur den eigenen Stack und die Abweichungen fest.[^17] Das Design-Dokument trägt Designhaltung, Designsystem, Interaktionsmuster und Visualisierungslogik als deklaratives Wissen, und die Sozialisierung eines Agents auf der ästhetischen Schicht entsteht dadurch, dass der Action Layer darauf verweist, und nicht durch Imperative im Dokument selbst.[^18] Wo ein Projekt Daten, Formate oder Zuständigkeiten über eine Grenze hinweg teilt, hält ein Integration-Dokument den aktuell gültigen Kontrakt, wobei genau eine Seite als Quelle der Wahrheit deklariert ist, wenn beide Seiten ihn beschreiben.[^19]

Zwei Dokumente tragen den Prozess. Ein Plan ordnet ausstehende Arbeit in Milestones, deren Exit-Bedingungen gegen Akzeptanzkriterien oder Quality Gates der Specification verankert und als Done-when-Aussagen formuliert sind.[^20] Ein Journal ist der kuratierte rückwärtsgerichtete Index der Übergänge und hält pro Übergang fest, ob das Ergebnis integriert, verworfen oder korrigiert wurde, ohne aktuellen Status, offene Aufgaben oder ausführliche Prüfresultate zu führen.[^21] Dazwischen steht die Process Inbox, die ausschließlich offene Übergabepunkte führt und deren Bearbeitung dauerhaften Inhalt in das zuständige Dokument integriert, den kurzen Nachweis im Journal schreibt und den Punkt danach vollständig entfernt.[^22]

Der Action Layer ist das eine Dokument, das allein für den Agenten geschrieben ist. Er routet in die Wissensbasis und übersetzt sie in Imperative, und weil er bei jedem Sessionstart injiziert wird, ist Drift hier teurer als anderswo, sodass jede aus Code oder Wissensbasis ableitbare Zeile gestrichen statt gepflegt wird.[^23] Sein Methodenkern aus Routing, Handoff-Bearbeitung, Provenienzregeln, Prüfregeln, Designprinzipien, Scope und Wahrheitshierarchie überlebt einen Wechsel des Coding-Agenten, und nur der werkzeugspezifische Block wird getauscht.[^24]

Zwei weitere Dokumente liegen an den Rändern des Satzes. Ein Statusbericht ist der einzige Dokumenttyp mit externem Adressaten und unterscheidet sich vom Journal durch Lebenszyklus und Kuratierungsgrad statt durch den Inhalt.[^25] Ein Governance-Dokument ist optional und kommt dort hinzu, wo Agents über mehrere persistente Ressourcen hinweg handeln oder folgenreiche Ansprüche, Rechte und Freigaben berühren, und hält Autorität, Berechtigungen, Evidenzstatus, Write-back-Ziele und Eskalationswege fest.[^26]

Was nicht in den Satz gehört, ist ebenso bestimmt. Derived Project Artefacts sind reproduzierbar erzeugte Ausgaben aus einem referenzierten Projektstand über ein identifiziertes Verfahren, und sie halten abgeleitete Beobachtungen fest statt Interpretationen oder Entscheidungen, die Beteiligte geprüft und übernommen haben, was sie außerhalb des gepflegten Wissens hält.[^27]

## Wann Distillation fertig ist

Das Abschlusskriterium ist praktisch. Eine neue mitarbeitende Person oder eine neue Agent-Instanz sollte mit den einschlägigen Wissensdokumenten und Zugriff auf die Projektressourcen die aktuelle Logik des Projekts rekonstruieren und die zugewiesene Arbeit ohne undokumentierte Erklärung fortsetzen können, und Schwierigkeiten dabei legen Auslassungen im gepflegten Bericht offen.[^28] Das Kriterium garantiert keine Vollständigkeit, und es macht Lücken an der Stelle sichtbar, an der der Agent nicht handeln kann oder einen Output erzeugt, der den fehlenden Kontext verrät. Eine gelungene Implementierung belegt nichts über wissenschaftliche Angemessenheit, weil eine Spezifikation ausführbar sein kann und dabei auf Annahmen ruht, die sich nicht rechtfertigen lassen.[^28]

## Gaps
- Die Vorlagen beschreiben einen erheblich größeren Dokumentensatz als die drei Typen, die das Paper nennt, und die Topic Map hält die offene Frage fest, ob das Buch den vollen Satz oder die Typologie mit den Vorlagen als deren Instanz darstellt. Dieses Kapitel stellt beides dar und entscheidet die Frage nicht.
- Die Vorlagen sind auf Deutsch mit englischen Funktionsnamen geschrieben. Welche ihrer Begriffe das Buch unübersetzt trägt, ist offen; das Kapitel verwendet durchgehend beschreibende Namen als vorläufige Setzung.
- Kapitel 7 des Skriptums behandelt dasselbe Material für ein Lehrpublikum und gehört zur parallelen Lane, sodass kein Vergleich mit dessen Fassung des Dokumentensatzes möglich war.
- Das Verification-Dokument ist hier als Mitglied des Satzes genannt und wird in Kapitel 16 behandelt, wo die Prüfformen Gegenstand sind.

[^1]: Grounded in [[30_assertions/distillation-is-the-documentary-operation-of-context-engineering]].
[^2]: Grounded in [[30_assertions/distillation-is-not-summarisation-or-compression]].
[^3]: Grounded in [[30_assertions/the-knowledge-base-differs-from-the-working-context]].
[^4]: Grounded in [[30_assertions/the-knowledge-base-is-a-set-of-interrelated-documents]].
[^5]: Grounded in [[30_assertions/declarative-documents-state-what-the-project-takes-to-be-the-case]].
[^6]: Grounded in [[30_assertions/process-documents-preserve-how-the-understanding-developed]].
[^7]: Grounded in [[30_assertions/agent-instruction-documents-translate-knowledge-into-imperatives]].
[^8]: Grounded in [[30_assertions/a-wrong-output-is-diagnosed-by-document-type]].
[^9]: Grounded in [[30_assertions/the-index-routes-a-knowledge-base]].
[^10]: Grounded in [[30_assertions/the-agent-enters-the-knowledge-base-through-its-index]].
[^11]: Grounded in [[30_assertions/the-charter-carries-the-project-identity]].
[^12]: Grounded in [[30_assertions/the-material-document-carries-epistemic-responsibility]].
[^13]: Grounded in [[30_assertions/domain-knowledge-carries-disciplinary-stipulation]].
[^14]: Grounded in [[30_assertions/an-outdated-rule-set-is-the-costliest-decay]].
[^15]: Grounded in [[30_assertions/the-specification-holds-interlocked-questions-in-one-place]].
[^16]: Grounded in [[30_assertions/the-architecture-document-gives-the-agent-its-module-boundaries]].
[^17]: Grounded in [[30_assertions/a-technology-baseline-carries-a-family-of-artefacts]].
[^18]: Grounded in [[30_assertions/design-knowledge-stays-declarative]].
[^19]: Grounded in [[30_assertions/the-integration-document-holds-the-contract-at-the-boundary]].
[^20]: Grounded in [[30_assertions/the-plan-is-the-forward-looking-counterpart-of-the-journal]].
[^21]: Grounded in [[30_assertions/the-journal-is-a-curated-provenance-index]].
[^22]: Grounded in [[30_assertions/the-handoff-document-is-a-process-inbox]].
[^23]: Grounded in [[30_assertions/the-action-layer-is-injected-and-therefore-kept-thin]].
[^24]: Grounded in [[30_assertions/the-method-core-of-the-action-layer-is-portable]].
[^25]: Grounded in [[30_assertions/the-report-addresses-an-external-reader]].
[^26]: Grounded in [[30_assertions/a-governance-document-records-authority-and-permissions]].
[^27]: Grounded in [[30_assertions/derived-artefacts-are-not-maintained-knowledge]].
[^28]: Grounded in [[30_assertions/the-sufficiency-of-distillation-is-practical]].
