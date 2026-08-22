---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-research-artefact-is-a-project-specific-operational-form]]", "[[30_assertions/acceptance-is-purpose-specific-and-bounded]]", "[[30_assertions/acceptance-rests-with-the-critical-expert]]", "[[30_assertions/data-governance-bounds-what-may-be-processed]]", "[[30_assertions/formal-modelling-does-not-determine-the-operational-form]]", "[[30_assertions/promptotyping-can-begin-from-three-project-conditions]]", "[[30_assertions/the-account-must-be-proportionate-to-what-is-delegated]]", "[[30_assertions/the-boundary-to-research-software-engineering]]", "[[30_assertions/the-method-cannot-supply-missing-competence]]", "[[30_assertions/the-method-redistributes-implementation-labour]]", "[[30_assertions/the-sufficiency-of-distillation-is-practical]]"]
posits: 1
lang: de
part: "IV. Promptotyping"
chapter: 12
title: "Voraussetzungen, Geltungsbereich und Verhältnis zum Research Software Engineering"
topic: "[[Promptotyping]]"
feeding-sources: ["paper chapter 2", "script chapter 7", "Promptotyping document templates"]
working-title: true
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Voraussetzungen, Geltungsbereich und Verhältnis zum Research Software Engineering

## Was vorhanden sein muss

Eine Methode, die den Preis der Implementierung senkt, senkt nicht den Preis des Wissens darüber, was implementiert werden soll. Promptotyping setzt Forschungsmaterial voraus, das strukturiert oder hinreichend semi-strukturiert ist, um computationell explizit gemacht zu werden, denn ein digitales Forschungsartefakt ist eine operative Form der Arbeit mit solchen Daten für einen definierten wissenschaftlichen Zweck.[^1] Es setzt fachliche Expertise voraus, die ausreicht, dieses Material zu kontextualisieren und zu beurteilen, denn die Methode unterstützt die Artikulation, Implementierung und Revision eines bereits vorhandenen Verständnisses und kann kein Domänenwissen liefern, das die Beteiligten nicht besitzen oder nicht als einschlägig erkennen.[^2] Vorlagen und gepflegte Dokumente machen Annahmen explizit und revidierbar, was etwas anderes ist, als die Annahmen bereitzustellen.[^2]

Es setzt eine prüfbare Wissensschicht voraus, und dafür gibt es einen praktischen Test. Eine neue mitarbeitende Person oder eine neue Agent-Instanz sollte mit den gepflegten Dokumenten und Zugriff auf die Projektressourcen die aktuelle Logik des Projekts rekonstruieren und die zugewiesene Arbeit ohne undokumentierte Erklärung fortsetzen können.[^3] Wo das misslingt, ist die Schicht noch nicht das, was die Methode verlangt.

Es setzt die Fähigkeit voraus, Anforderungen zu formulieren, was hier heißt, wissenschaftliche Praxis in Aussagen zu übersetzen, die eine Implementierung anleiten, ohne ihren Forschungszweck zu verlieren. Und es setzt Prüfkapazität voraus, denn die Abnahme liegt bei einer Person oder Gruppe, die kompetent und verantwortlich beurteilt, ob das Projektwissen das Forschungsmaterial angemessen repräsentiert und ob das Artefakt für seinen Zweck taugt.[^4] Ein Projekt, das dieses Urteil nicht besetzen kann, hat keine Möglichkeit, eine Iteration abzuschließen.

Die formale Aufbereitung der Daten ersetzt nichts davon. Modellierung und FAIR-Aufbereitung stützen Maschinenverarbeitbarkeit, Interoperabilität und Nachnutzung und lassen offen, wie in einem bestimmten Projekt mit den Daten gearbeitet werden soll, weil dieselben Daten verschiedene Fragen tragen können und dafür verschiedene operative Formen brauchen.[^5] Die beiden gegensätzlichen Untersuchungen, die aus einem gemeinsamen Modell historischer Buchhaltungstransaktionen hervorgingen, zeigen das konkret, denn die interoperable Repräsentation trug beide und bestimmte keine von beiden.[^5]

## Die Lücke, auf die die Methode antwortet

Die Übersetzung wissenschaftlicher Anforderungen in Software lief üblicherweise über die Zusammenarbeit von Fachwissenschaft und technischer Seite, und diese Zusammenarbeit bleibt für Artefakte unverzichtbar, die verlässlichen Dauerbetrieb, institutionelle Integration, Sicherheit oder unterstützte Nutzung durch Dritte verlangen. Die dafür nötige Expertise und die dafür nötigen Ressourcen stehen einzelnen Forschenden und kleinen Projekten nicht gleichermaßen zur Verfügung.[^6] Promptotyping antwortet auf die begrenzte Kapazitätslücke, die sich zwischen einer Person, die Domänenwissen und Forschungsanforderungen artikulieren kann, und den technischen Mitteln zur Realisierung einer projektspezifischen Form auftut.

Die Lücke ist nach beiden Seiten begrenzt. Auf der einen Seite hat die Methode eine Eintrittsbedingung und keinen festen Startpunkt, denn sie kann von einem etablierten Forschungsdatenstand ausgehen, an dessen Entwicklung teilnehmen oder eine geplante Anordnung operationalisieren, bevor ein Produktionskorpus existiert.[^7] Auf der anderen Seite wird der adressierte Aufwand umverteilt statt beseitigt. Ein Agent kann rasch ein erstes funktionsfähiges Artefakt herstellen, während Fachwissenschaft weiterhin Anforderungen spezifiziert, Outputs prüft, Abweichungen interpretiert und über die Abnahme entscheidet, und während Research Software Engineers die Implementierung später für den verlässlichen Betrieb umbauen müssen.[^8]

Wie viel dokumentarische Arbeit die Methode verlangt, folgt daraus, was delegiert wird. Eine begrenzte Transformation auf einem stabilen und gut verstandenen Format lässt sich mit knappen Mappings und formalen Prüfungen anleiten. Arbeit, die Interpretation, Modellierung, Implementierung und Prüfung umspannt, verlangt einen expliziten Bericht über Quellen, Annahmen, Anforderungen und Grenzen.[^9] Die Regel ist Verhältnismäßigkeit, und die schwere Form auf den leichten Fall anzuwenden verbraucht genau die Kapazität, die die Methode freisetzen sollte.

## Wohin die Methode nicht reicht

Promptotyping ersetzt die Zusammenarbeit mit Research Software Engineers oder anderen technischen Spezialistinnen und Spezialisten nicht. Artefakte für den verlässlichen institutionellen oder öffentlichen Betrieb verlangen weiterhin Expertise in Sicherheit, Barrierefreiheit, Wartbarkeit, Integration und Dauerbetrieb, und die Methode ist unangemessen, wo Beteiligte das Verhältnis von Quellen, Forschungsdaten, gepflegtem Projektwissen, Implementierung und Output nicht rekonstruieren oder beurteilen können.[^6] Eine gesenkte Implementierungsschwelle ist keine Lizenz für Artefakte, deren Grundlagen, Grenzen, Zuständigkeiten und Status sich nicht verantwortbar machen lassen.[^6]

Eine zweite Grenze ist rechtlich und institutionell statt technisch. Die Methode erteilt keine allgemeine Erlaubnis, Forschungsmaterial an externe generative Systeme zu übergeben, die Zulässigkeit hängt vom Material und von den geltenden rechtlichen, institutionellen und architektonischen Bedingungen ab, eingeschränktes oder personenbezogenes Material kann geprüfte lokale Verarbeitung oder Ausschluss verlangen, der Zugriff eines Agents auf Projektressourcen wird über kontrollierte Berechtigungen und zurechenbare Aktionen begrenzt, und zweckgebundene wissenschaftliche Abnahme ersetzt die institutionelle Verantwortung für sicheren, nachhaltigen und rechtskonformen Betrieb nicht.[^10]

Eine dritte Grenze betrifft die Kompetenz und zeigt sich erst im Nachhinein. Unzureichendes Projektwissen kann einen Agent zu einer Implementierung führen, die kohärent und funktionsfähig ist und in wissenschaftlicher Hinsicht unzureichend bleibt, weshalb verantwortliche Anwendung eine kritische Prüfung von Provenienz, Konstruktion, Reichweite und Repräsentationsgrenzen der Daten verlangt, bevor das Artefakt gebaut wird, statt nachdem es überzeugt.[^2]

## Der Übergang zum Research Software Engineering

Die Grenze ist überschritten, sobald sich die Pflichten ändern, die an einem Artefakt hängen. Eine explorative Oberfläche, die ihre Autorin selbst benutzt, trägt wenige davon. Ein Artefakt, das dauerhaft, gewartet, sicher, barrierefrei, institutionell betrieben, von mehreren geteilt, auf persistenten serverseitigen Zustand angewiesen, in externe Infrastruktur integriert oder für Dritte unterstützt sein muss, trägt die meisten davon gleichzeitig, und jede ist eine eigene Kompetenz.[^6] Die Änderung betrifft die Pflichten und nicht den Umfang, weshalb ein kleines Artefakt die Grenze überschreiten und ein großes innerhalb bleiben kann.

Die zweckgebundene Abnahme macht den Übergang lesbar. Eine Iteration kann als experimentelle Verarbeitungsstrecke, als internes Workflow-Werkzeug, als Demonstrator für einen Antrag oder als Übergabestand abgenommen werden, und keine dieser Abnahmen behauptet Produktionsreife.[^11] Wo der abgenommene Zweck auf institutionellen Betrieb wechselt, ist das Artefakt in den Bereich des Research Software Engineering eingetreten, unabhängig davon, ob sich sein Code geändert hat.

Promptotyping Documents können die Übergabe prüfbarer machen, weil die aufnehmende Seite Forschungskontext, Quellen- und Datenbeschreibungen, Anforderungen, Designentscheidungen, Prüfkonzepte, bekannte Grenzen, Prozessgeschichte und offene Fragen bereits aufgeschrieben vorfindet, statt sie aus dem Code zu rekonstruieren.[^12] Was sie nicht leisten, ist die Expertise und die Ressourcen zu ersetzen, die nachhaltige Forschungssoftware verlangt.[^6]

## Gaps
- Die Zusammensetzung eines Übergabepakets steht in der Gliederung und wird von keiner Quelle dieses Vaults getragen. Das Kapitel behandelt sie deshalb als eigene Schlussfolgerung; eine verankerte Behandlung setzt voraus, dass die Vorlagen eines übergabeorientierten Dokumentensatzes als Quellstellen aufgenommen werden oder das Skriptum der parallelen Lane vorliegt.
- Die Liste der Pflichten, die den Übergang zum Research Software Engineering markieren, stammt aus dem Exposé. Das Paper nennt dieselben Pflichten in Prosa, ohne sie aufzuzählen, sodass die Aufzählung dieses Kapitels der Gliederung folgt und sachlich auf einer Assertion ruht.
- Requirements Engineering als Voraussetzung ist hier in den Begriffen der Methode beschrieben. Eine Behandlung, die die Literatur des Requirements Engineering direkt zitiert, setzt voraus, dass diese Publikationen als Quellen registriert werden.

[^1]: Grounded in [[30_assertions/a-research-artefact-is-a-project-specific-operational-form]].
[^2]: Grounded in [[30_assertions/the-method-cannot-supply-missing-competence]].
[^3]: Grounded in [[30_assertions/the-sufficiency-of-distillation-is-practical]].
[^4]: Grounded in [[30_assertions/acceptance-rests-with-the-critical-expert]].
[^5]: Grounded in [[30_assertions/formal-modelling-does-not-determine-the-operational-form]].
[^6]: Grounded in [[30_assertions/the-boundary-to-research-software-engineering]].
[^7]: Grounded in [[30_assertions/promptotyping-can-begin-from-three-project-conditions]].
[^8]: Grounded in [[30_assertions/the-method-redistributes-implementation-labour]].
[^9]: Grounded in [[30_assertions/the-account-must-be-proportionate-to-what-is-delegated]].
[^10]: Grounded in [[30_assertions/data-governance-bounds-what-may-be-processed]].
[^11]: Grounded in [[30_assertions/acceptance-is-purpose-specific-and-bounded]].
[^12]: Posit: ein aus den gepflegten Dokumenten zusammengestelltes Übergabepaket verbilligt die Rekonstruktion auf der aufnehmenden Seite, weil das Material, das sie sonst aus dem Code erschließen müsste, bereits für die Prüfung geschrieben vorliegt. Open evidence question: eine dokumentierte Übergabe, in der ein aufnehmendes Team festgehalten hat, was die gepflegten Dokumente beantwortet haben und was es dennoch rekonstruieren musste.