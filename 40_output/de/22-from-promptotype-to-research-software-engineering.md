---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-demonstrator-can-carry-a-project-before-its-corpus-exists]]", "[[30_assertions/acceptance-is-purpose-specific-and-bounded]]", "[[30_assertions/data-governance-bounds-what-may-be-processed]]", "[[30_assertions/promptotype-evaluation-separates-conformity-adequacy-and-purpose]]", "[[30_assertions/proprietary-dependence-limits-durability]]", "[[30_assertions/the-accepted-state-must-remain-identifiable]]", "[[30_assertions/the-account-must-be-proportionate-to-what-is-delegated]]", "[[30_assertions/the-benefit-of-the-method-is-distributed-unevenly]]", "[[30_assertions/the-boundary-to-research-software-engineering]]", "[[30_assertions/the-handoff-document-is-a-process-inbox]]", "[[30_assertions/the-integration-document-holds-the-contract-at-the-boundary]]", "[[30_assertions/the-method-redistributes-implementation-labour]]", "[[30_assertions/the-provenance-of-a-generated-process-is-documentary]]", "[[30_assertions/the-report-addresses-an-external-reader]]"]
posits: 3
lang: de
part: "VI. Worked Example, Boundaries, and Implications"
chapter: 22
title: "Vom Promptotype zum Research Software Engineering"
topic: "[[Boundaries-and-Implications]]"
feeding-sources: ["paper chapter 4", "hands-on chains from slides and script"]
working-title: true
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Vom Promptotype zum Research Software Engineering

## Die Grenze ist ein Wechsel der Pflichten

Die technische und organisatorische Grenze des Promptotyping ist erreicht, sobald sich die Pflichten ändern, die an einem Artefakt hängen. Die Zusammenarbeit mit Research Software Engineers bleibt für Artefakte unverzichtbar, die verlässlichen Dauerbetrieb, institutionelle Integration, Sicherheit oder unterstützte Nutzung durch Dritte verlangen, Expertise und Ressourcen dafür sind ungleich verteilt, und die Methode ist unangemessen, wo Beteiligte das Verhältnis von Quellen, Forschungsdaten, gepflegtem Wissen, Implementierung und Output nicht rekonstruieren oder beurteilen können.[^1]

Von innen erkennbar wird die Grenze am abgenommenen Zweck. Die Abnahme ist zweckgebunden und begrenzt, ein Artefakt kann also als experimentelle Verarbeitungsstrecke, als internes Workflow-Werkzeug, als Demonstrator für einen Antrag oder als Übergabestand abgenommen sein, ohne dass eine dieser Abnahmen Produktionsreife behauptet.[^2] Ein Wechsel des abgenommenen Zwecks hin zum institutionellen Betrieb schiebt das Artefakt über die Grenze, unabhängig davon, ob sich eine Zeile Code ändert. Die Bewertung ändert sich mit, denn technische Konformität, wissenschaftliche Angemessenheit und Eignung für den erklärten Zweck sind getrennte Fragen, und ein exploratives Artefakt muss keine Produktionskriterien erfüllen, die außerhalb seines abgenommenen Umfangs liegen.[^3]

## Warum statisch und in sich geschlossen oft die richtige Form ist

Für begrenzte Forschungszwecke ist ein statisches, in sich geschlossenes Artefakt oft angemessen, weil es lokal laufen, über statisches Hosting ausgeliefert werden, persistente Backend-Infrastruktur vermeiden, Abhängigkeitsketten verkürzen, prüfbar bleiben und Archivierung tragen kann.[^4] Der dokumentierte Fall aus der Antragsphase hatte genau diese Form, denn ein begrenzter Weg führte von einer kleinen Textprobe über eine kodierte Repräsentation zu einem statisch gehosteten Edition Interface, das eine vorgeschlagene Anordnung prüfbar machte, ohne eine Produktionsinfrastruktur dahinter.[^5] Die Form passt außerdem zur Dauerhaftigkeitsanforderung eines abgenommenen Zustands, der über ein Release, eine archivierte Ablage oder eine andere dauerhafte Referenz identifizierbar und rekonstruierbar bleiben muss.[^6]

Die Grenzen der Form sind ebenso bestimmt. Browserspeicher und rechenintensive Verarbeitung begrenzen, was ein in sich geschlossenes Artefakt verarbeiten kann, und geteilter Zustand, Authentifizierung, gleichzeitiges Bearbeiten, persistentes Schreiben, Sicherheitsanforderungen, Barrierefreiheitspflichten und fortlaufende institutionelle Unterstützung führen jeweils eine Pflicht ein, die die Form nicht trägt.[^4] Wo diese für die Aufgabe des Artefakts zentral werden, ist das Artefakt in den Bereich des Research Software Engineering eingetreten.

Zwei Randbedingungen aus früheren Kapiteln wirken auf dieselbe Entscheidung. Data Governance begrenzt, welche Materialien und Workflows überhaupt verwendet werden dürfen, denn die Zulässigkeit hängt vom Material und von rechtlichen, institutionellen und architektonischen Bedingungen ab, der Zugriff eines Agents muss über kontrollierte Berechtigungen und zurechenbare Aktionen begrenzt sein, und zweckgebundene wissenschaftliche Abnahme ersetzt die institutionelle Verantwortung für sicheren, nachhaltigen und rechtskonformen Betrieb nicht.[^7] Und die Abhängigkeit von proprietären Frontier-Systemen bringt direkte Kosten, verringert die Kontrolle über Systemänderungen und steht in Spannung zu der Prüfbarkeit, Reproduzierbarkeit und Dauerhaftigkeit, die Forschungssoftware anstrebt, denn Änderungen an Modell und Harness können das Verhalten ändern, während Projektwissen und Daten stabil bleiben.[^8]

## Die Übergabe

Eine Übergabe an das professionelle Engineering ist ein Kontrakt an einer Projektgrenze, und die Methode hat für diese Gestalt bereits einen Dokumenttyp, der das aktuell gültige Austauschformat, die Zuständigkeiten und die Abnahmekriterien hält, wobei genau eine Seite als Quelle der Wahrheit deklariert ist, wenn beide Seiten ihn beschreiben.[^9] Was eine solche Übergabe enthalten muss, folgt daraus, was die aufnehmende Seite sonst aus dem Code rekonstruieren müsste, also Forschungskontext, Quellen- und Datenbeschreibungen, Anforderungen, Designentscheidungen, Test- und Prüfkonzepte, bekannte Grenzen, Abhängigkeitsinventar, Prozessgeschichte, Provenienz und offene Fragen.[^10]

Das meiste davon liegt in einem so arbeitenden Projekt bereits geschrieben vor. Das Materialdokument trägt Quellen- und Datenbeschreibungen, die Specification trägt Anforderungen und Entscheidungen, das Design-Dokument trägt die Repräsentationsentscheidungen, das Testdokument trägt Garantien und bewusste Lücken, der Provenienznachweis trägt die Geschichte der Übergänge mit ihren Verdikten, und die Process Inbox trägt, was noch offen ist.[^11] Der Provenienznachweis verdient bei einer Übergabe besondere Aufmerksamkeit, denn wo Interaktionsprotokolle nicht aufbewahrt werden, besteht die dauerhafte Provenienz eines generativen Prozesses aus dem gepflegten Wissen, dem Arbeitsnachweis, den Quellen, den dokumentierten Entscheidungen und der Versionsgeschichte, und dieses Material kann nicht jede verworfene Alternative und nicht jedes Element stillschweigenden Urteils wiedergeben.[^12] Ein aufnehmendes Team, das das weiß, liest den Nachweis auf das, was er trägt, und nicht auf das, was er zu versprechen scheint.

Ein Dokumenttyp des Satzes ist für genau diesen Adressaten geschrieben. Ein Statusbericht ist das einzige Dokument der Methode mit externer Leserschaft, das einen Stand für eine dritte Person ohne Repo-Vorwissen verdichtet und sich vom internen Provenienznachweis durch Lebenszyklus und Kuratierung unterscheidet und nicht durch den Inhalt.[^13]

## Was eine Übergabe nicht beseitigt

Promptotyping kann eine Übergabe prüfbarer machen, und es kann die Expertise und die Ressourcen nicht beseitigen, die nachhaltige Forschungssoftware verlangt.[^1] Die Umverteilung der Arbeit ist der Grund, das deutlich zu sagen. Ein Agent kann rasch ein funktionsfähiges Artefakt herstellen, während Fachwissenschaft weiterhin spezifiziert, prüft, interpretiert und abnimmt, und während Research Software Engineers die Implementierung später für den verlässlichen Betrieb umbauen, weshalb eine Evaluation verringerten Aufwand von verlagertem, neu entstandenem und aufgeschobenem Aufwand unterscheiden muss.[^14] Die aufnehmende Seite einer Übergabe ist der Ort, an dem aufgeschobener Aufwand ankommt, und die Rollen nehmen ihn ungleich auf, denn Research Software Engineers können technische Schulden erben, während die für die Prüfung Verantwortlichen plausibleren Outputs ohne entsprechende Mittel oder Autorität gegenüberstehen.[^15]

Die Verhältnismäßigkeitsregel gilt für die Übergabe wie für die Arbeit davor. Eine begrenzte Transformation auf einem stabilen Format wird mit knappen Mappings und formalen Prüfungen übergeben, während Arbeit, die Interpretation, Modellierung, Implementierung und Prüfung umspannt, einen expliziten Bericht über Quellen, Annahmen, Anforderungen und Grenzen übergibt.[^16] Mehr zu schreiben, als der Fall verlangt, verbraucht die Kapazität, die die Methode freisetzen sollte, und weniger zu schreiben verschiebt die Rekonstruktionskosten auf die aufnehmende Seite, ohne festzuhalten, dass sie verschoben wurden.[^17]

## Gaps
- Vorteile und Grenzen statischer, in sich geschlossener Artefakte sind in der Gliederung aufgezählt. Die Quellen tragen eine dokumentierte Instanz der Form und das allgemeine Grenzkriterium, sodass die Aufzählungen hier auf der Gliederung ruhen und als solche markiert sind.
- Die Zusammensetzung eines Übergabepakets stammt ebenfalls aus der Gliederung. Das Kapitel verankert jedes Element in dem Dokumenttyp, der es bereits hält, und behandelt die Liste selbst als eigene Anordnung des Buches.
- Die Hands-on-Ketten des Skriptums und des Foliensatzes speisen Teil VI und gehören zur parallelen Schreiblane, sodass kein durchgeführtes Übergabebeispiel vorlag.
- In den Quellen ist keine Übergabe an ein Research-Software-Engineering-Team beschrieben, weshalb die Wirkung der Anordnung auf ein aufnehmendes Team eine offene Evidenzfrage bleibt.

[^1]: Grounded in [[30_assertions/the-boundary-to-research-software-engineering]].
[^2]: Grounded in [[30_assertions/acceptance-is-purpose-specific-and-bounded]].
[^3]: Grounded in [[30_assertions/promptotype-evaluation-separates-conformity-adequacy-and-purpose]].
[^4]: Posit: Vorteile und Grenzen der statischen, in sich geschlossenen Form stehen in der Gliederung, und die Quellen benennen das Grenzkriterium, ohne die technischen Eigenschaften auf beiden Seiten aufzuzählen. Open evidence question: ein Vergleich dokumentierter Artefakte nach Auslieferungsform gegen die Pflichten, die jedes von ihnen tatsächlich zu tragen hatte.
[^5]: Grounded in [[30_assertions/a-demonstrator-can-carry-a-project-before-its-corpus-exists]].
[^6]: Grounded in [[30_assertions/the-accepted-state-must-remain-identifiable]].
[^7]: Grounded in [[30_assertions/data-governance-bounds-what-may-be-processed]].
[^8]: Grounded in [[30_assertions/proprietary-dependence-limits-durability]].
[^9]: Grounded in [[30_assertions/the-integration-document-holds-the-contract-at-the-boundary]].
[^10]: Posit: der Inhalt eines Übergabepakets folgt daraus, was ein aufnehmendes Team sonst aus dem Code erschließen müsste, und die Gliederung führt ihn auf, ohne dass eine Quelle dieses Vaults die Liste trägt. Open evidence question: eine dokumentierte Übergabe, in der das aufnehmende Team festgehalten hat, welche dieser Elemente es genutzt hat und welche es dennoch rekonstruieren musste.
[^11]: Grounded in [[30_assertions/the-handoff-document-is-a-process-inbox]].
[^12]: Grounded in [[30_assertions/the-provenance-of-a-generated-process-is-documentary]].
[^13]: Grounded in [[30_assertions/the-report-addresses-an-external-reader]].
[^14]: Grounded in [[30_assertions/the-method-redistributes-implementation-labour]].
[^15]: Grounded in [[30_assertions/the-benefit-of-the-method-is-distributed-unevenly]].
[^16]: Grounded in [[30_assertions/the-account-must-be-proportionate-to-what-is-delegated]].
[^17]: Posit: eine unterdokumentierte Übergabe verschiebt die Rekonstruktionskosten stillschweigend, weil die aufnehmende Seite die Lücke erst beim Bezahlen bemerkt. Open evidence question: ob aufnehmende Teams solche Kosten in einer Form festhalten, die den Vergleich erlauben würde.
