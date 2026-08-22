---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/acceptance-rests-with-the-critical-expert]]", "[[30_assertions/amplification-rather-than-transfer-of-authority]]", "[[30_assertions/an-individual-account-is-not-evidence-for-others]]", "[[30_assertions/capable-systems-widen-the-span-between-production-and-acceptance]]", "[[30_assertions/critical-expert-verification-records-who-is-responsible]]", "[[30_assertions/critical-expertise-may-be-distributed-without-transferring-responsibility]]", "[[30_assertions/data-governance-bounds-what-may-be-processed]]", "[[30_assertions/deterministic-verification-is-bounded-by-its-checks]]", "[[30_assertions/no-claim-about-environmental-efficiency]]", "[[30_assertions/the-artefact-produces-no-knowledge-on-its-own]]", "[[30_assertions/the-benefit-of-the-method-is-distributed-unevenly]]", "[[30_assertions/the-boundary-to-research-software-engineering]]", "[[30_assertions/the-critical-expert-examines-what-a-coherent-artefact-conceals]]", "[[30_assertions/the-method-cannot-supply-missing-competence]]", "[[30_assertions/the-provenance-of-a-generated-process-is-documentary]]", "[[30_assertions/the-significance-is-modal-rather-than-economic]]", "[[30_assertions/the-sufficiency-of-distillation-is-practical]]"]
posits: 3
lang: de
part: "VI. Worked Example, Boundaries, and Implications"
chapter: 24
title: "Verstärkung, Verantwortung und die Grenzen der Externalisierung"
topic: "[[Boundaries-and-Implications]]"
feeding-sources: ["paper chapter 4", "hands-on chains from slides and script"]
working-title: true
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Verstärkung, Verantwortung und die Grenzen der Externalisierung

## Was externalisiert wird

Promptotyping externalisiert einen Teil der Übersetzung zwischen wissenschaftlichem Wissen und computationeller Implementierung. Gepflegte Dokumente halten fest, was das Projekt für den Fall hält, ein Agent implementiert daraus, und das Ergebnis wird gegen die Quellen geprüft und zurückgeschrieben. Was die Anordnung aus dem Kopf einer Person in eine prüfbare Form verlagert, ist der Bericht über die Daten, die Anforderungen, die Repräsentationsentscheidungen und die Prüfkriterien.

Die Grenze dieser Verlagerung ist in der Methode selbst formuliert. Die gepflegten Dokumente tragen die Artikulation, Implementierung und Revision eines bereits vorhandenen Verständnisses, und sie können kein Domänenwissen liefern, das die Beteiligten nicht besitzen oder nicht als einschlägig erkennen.[^1] Das Abschlusskriterium der Distillation misst die Dokumente an einer Aufgabe statt an Vollständigkeit, denn eine neue mitarbeitende Person oder eine neue Agent-Instanz soll die Logik des Projekts rekonstruieren und die Arbeit fortsetzen können, und Schwierigkeiten dabei legen Auslassungen offen.[^2] Nichts an diesem Kriterium verspricht, dass alles Einschlägige aufgeschrieben wurde.

Ein Teil dessen, was bleibt, entzieht sich der Dokumentation seiner Natur nach. Über Jahre gewachsene Vertrautheit mit einem Korpus, Gespür für die Ausnahmequelle, die nicht ins Schema passt, Bewusstsein dafür, in welche fachliche Debatte eine Modellierungsentscheidung eintritt, und das Erkennen einer fehlenden plausiblen Alternative sind Kompetenzen, die sich in Urteilen zeigen und nicht in Regeln.[^3] Der dokumentarische Nachweis eines generativen Prozesses registriert das indirekt, denn gepflegtes Wissen, Arbeitsnachweis, Quellen, Entscheidungen und Versionsgeschichte machen folgenreiche Stationen prüfbar, ohne jede verworfene Alternative und jedes Element stillschweigenden Urteils wiederzugeben.[^4]

## Verstärkung statt Automatisierung

Die Position der Methode lautet, dass der Beitrag LLM-basierter Agents zur wissenschaftlichen Arbeit Verstärkung ist und dass die wissenschaftliche Kompetenz und das verantwortete Urteil, die sie voraussetzt, unverzichtbar bleiben.[^5] Als empirischer Anspruch gelesen ist diese Position bescheiden, denn die dokumentierten Fälle zeigen nicht, dass die Methode Artefakte schneller, billiger oder verlässlicher hervorbringt als andere Vorgehensweisen, und was sie zeigen, ist, dass Formen projektspezifischer Implementierung, die bislang außerhalb der praktischen Mittel einzelner Forschender und kleiner Projekte lagen, überhaupt machbar wurden.[^6]

Was verstärkt wird, lässt sich einigermaßen genau benennen. Gepflegtes Projektwissen trägt das Verständnis eines Projekts über Sitzungen und über die Grenze zwischen Menschen und Agents hinweg, Anforderungen und Designentscheidungen werden nachnutzbar, weil sie dort stehen, wo man sie findet, die Implementierung bleibt prüfbar, weil die Inkremente versioniert und gegen die Dokumente vergleichbar sind, und der gesunkene Preis einer ersten funktionierenden Implementierung macht alternative computationelle Formen vergleichbar statt bloß denkbar.[^7] Die Reichweite einer Person, die sowohl eine wissenschaftliche Anforderung als auch eine technische Randbedingung artikulieren kann, wächst am stärksten, und das ist der Mechanismus hinter der ungleichen Verteilung des Nutzens.[^8]

Was nicht verstärkt wird, ist ebenso bestimmt. Die Methode ersetzt weder wissenschaftliche Expertise noch Quellenkritik noch Datenmodellierung, denn sie arbeitet an dem, was diese hervorbringen.[^1] Sie ersetzt keine formale Validierung, denn deterministische Prüfungen reichen genau so weit wie die Eigenschaften, die sie kodieren, und jemand muss entscheiden, welche Eigenschaften zählen.[^9] Sie ersetzt weder Security Engineering noch Barrierefreiheitsarbeit noch Wartung noch institutionelle Governance, denn das sind die Pflichten, die die Grenze zum Research Software Engineering markieren.[^10] Und sie ersetzt nicht die Verantwortung für veröffentlichte Behauptungen.[^5]

Eine Asymmetrie durchzieht all das und wächst, statt zu schrumpfen. Mit dem Umfang, der Reichweite und der Plausibilität delegierbarer Arbeit wächst der Abstand zwischen dem, was Agents herstellen können, und dem, was Forschende verantwortbar annehmen können, und gepflegtes Wissen, differenzierte Prüfung, Write-back und zweckgebundene Abnahme sind die Mittel, mit denen dieser Abstand steuerbar bleibt.[^11] Leistungsfähigere Systeme erhöhen damit den Wert der Anordnung, statt sie überflüssig zu machen.

## Wo die Verantwortung sitzt

Verantwortung folgt aus Abnahme und Veröffentlichung.[^12] Sie folgt nicht daraus, etwas von Hand hergestellt zu haben. Das ist der Erwähnung wert, weil die Intuition in die andere Richtung läuft und weil ein Arbeitsablauf, in dem der größte Teil des Codes generiert wurde, die Annahme nahelegt, die Verantwortung sei mitgeneriert worden.

Die Methode verortet Verantwortung genau. Die Abnahme liegt beim Critical Expert, also bei der Person oder Gruppe, die kompetent und verantwortlich beurteilt, ob das Projektwissen das Forschungsmaterial angemessen repräsentiert und ob das Artefakt für seinen Zweck taugt, und ein Agent kann Vorschläge und Einschätzungen beitragen, ohne Verantwortung für deren Angemessenheit zu übernehmen.[^13] Die Verifikation durch diese Rolle hält fest, wer die Verantwortung für das Urteil übernimmt, was eine abstrakte Zurechenbarkeit in einen Namen mit Datum verwandelt.[^14] Eine Verteilung auf mehrere Personen ändert, wer welchen Teil hält, und überträgt nichts, und eine Verteilung auf mehrere Agents ändert die Koordination und hält Zuweisungen, Berechtigungen und Ausgaben auditierbar.[^15]

Zwei weitere Grenzen bestimmen, was Abnahme heißen kann. Zweckgebundene wissenschaftliche Abnahme ersetzt die institutionelle Verantwortung für sicheren, nachhaltigen und rechtskonformen Betrieb nicht, und die Zulässigkeit von Material und Arbeitsablauf wird außerhalb der Methode entschieden.[^16] Und ein für einen erklärten Zweck abgenommenes Artefakt behauptet nichts darüber hinaus, weshalb eine Prüfung fragen muss, ob einschlägige Alternativen ausgeschlossen, Konventionen ohne Begründung reproduziert oder Fehlstellen von einem kohärent wirkenden Artefakt verdeckt wurden.[^17]

## Die ehrliche Form des Anspruchs

Zwei Aussagen müssen am Ende dieses Teils zusammen stehen. Die in diesem Buch beschriebene Anordnung hat bestimmte Arbeit für Personen möglich gemacht, die sie zuvor nicht leisten konnten, und die Evidenz für ihre Wirkungen ist dünn, und zwar aus Anlage und nicht aus Nachlässigkeit. Die Ressourcenfrage ist offen, denn der Ressourcenverbrauch von Modellen, wiederholten Generierungen, Auslieferungsarchitekturen und alternativen Arbeitsabläufen wurde nicht vergleichend gemessen, und ein gesunkener Entwicklungsaufwand belegt daher keinen gesunkenen Verbrauch.[^18] Die Erfahrungsfrage ist auf dieselbe Weise offen, denn der Bericht einer Autorschaft über einen verstärkten Arbeitsprozess beschreibt, wie eine Person die Arbeit organisiert hat, und ist keine Evidenz über andere.[^19]

Beides im Blick zu behalten hält die Methode zur Methode. Ein Artefakt bringt für sich kein wissenschaftliches Wissen hervor, und seine epistemische Relevanz entsteht über Operationalisierung, Prüfung, Interpretation, Zuordnung und Write-back.[^20] Dasselbe gilt für die Anordnung, die Artefakte hervorbringt.

## Gaps
- Die Liste dessen, was sich der Dokumentation entzieht, von der stillschweigenden Vertrautheit mit einem Korpus bis zum Erkennen fehlender Alternativen, stammt aus der Gliederung. Die Quellen benennen stillschweigendes Urteil als etwas, das der Nachweis nicht wiedergeben kann, ohne dessen Formen aufzuzählen, sodass die Aufzählung hier als eigene geführt wird.
- Die Listen dessen, was die Methode verstärkt und was sie nicht ersetzt, stammen ebenfalls aus der Gliederung. Jeder Punkt ist hier in der Assertion verankert, die ihn trägt, und die Listen selbst sind die Anordnung des Buches.
- Die Hands-on-Ketten des Skriptums und des Foliensatzes speisen Teil VI und gehören zur parallelen Schreiblane, sodass die didaktische Perspektive auf Verantwortung in diesem Kapitel fehlt.

[^1]: Grounded in [[30_assertions/the-method-cannot-supply-missing-competence]].
[^2]: Grounded in [[30_assertions/the-sufficiency-of-distillation-is-practical]].
[^3]: Posit: die vier hier benannten Kompetenzformen sind die eigene Ausbuchstabierung dessen, was die Quellen stillschweigendes Urteil nennen, und keine Quelle zählt sie auf. Open evidence question: ob Fortsetzungsstudien Fehlschläge aus undokumentiertem stillschweigendem Wissen von Fehlschlägen aus dokumentarischer Auslassung unterscheiden können.
[^4]: Grounded in [[30_assertions/the-provenance-of-a-generated-process-is-documentary]].
[^5]: Grounded in [[30_assertions/amplification-rather-than-transfer-of-authority]].
[^6]: Grounded in [[30_assertions/the-significance-is-modal-rather-than-economic]].
[^7]: Posit: die vier als verstärkt benannten Punkte folgen aus den Mechanismen, die die vorangegangenen Kapitel festhalten, also gepflegtes Wissen über Sitzungen hinweg, geschriebene Anforderungen und Entscheidungen, versionierte prüfbare Inkremente und ein gesunkener Preis der ersten Implementierung. Open evidence question: ob sich einer der vier gegen eine Vergleichsbedingung ohne die Methode messen lässt.
[^8]: Grounded in [[30_assertions/the-benefit-of-the-method-is-distributed-unevenly]].
[^9]: Grounded in [[30_assertions/deterministic-verification-is-bounded-by-its-checks]].
[^10]: Grounded in [[30_assertions/the-boundary-to-research-software-engineering]].
[^11]: Grounded in [[30_assertions/capable-systems-widen-the-span-between-production-and-acceptance]].
[^12]: Posit: die Verantwortung an Abnahme und Veröffentlichung statt an die manuelle Herstellung zu binden, folgt daraus, dass die Methode die Abnahme bei einer verantwortlichen Rolle verortet und festhält, wer sie übernimmt. Open evidence question: ob Forschungseinrichtungen Verantwortung dort ebenso zurechnen, wo ein Output weitgehend generiert wurde.
[^13]: Grounded in [[30_assertions/acceptance-rests-with-the-critical-expert]].
[^14]: Grounded in [[30_assertions/critical-expert-verification-records-who-is-responsible]].
[^15]: Grounded in [[30_assertions/critical-expertise-may-be-distributed-without-transferring-responsibility]].
[^16]: Grounded in [[30_assertions/data-governance-bounds-what-may-be-processed]].
[^17]: Grounded in [[30_assertions/the-critical-expert-examines-what-a-coherent-artefact-conceals]].
[^18]: Grounded in [[30_assertions/no-claim-about-environmental-efficiency]].
[^19]: Grounded in [[30_assertions/an-individual-account-is-not-evidence-for-others]].
[^20]: Grounded in [[30_assertions/the-artefact-produces-no-knowledge-on-its-own]].
