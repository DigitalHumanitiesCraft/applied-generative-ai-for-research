---
type: knowledge
created: 2026-01-18
updated: 2026-07-23
tags: [knowledge-engineering, original]
status: complete
aliases: [Wissensdokument, Wissensdokumente, Wissensdokumente als Speicherformat, Wissenstransformationen in Obsidian]
---

# Vault als materialisiertes Wissensmodell

## Summary

Ein Obsidian-Vault ist mehr als ein Speicherort für Notizen. Er ist ein materialisiertes semantisches Netz, dessen Struktur aus Links, Tags und Hierarchien selbst Bedeutung trägt und das sich selektiv in LLM-Kontexte einspeisen lässt. Wer den Vault als Wissensmodell begreift, versteht jede Vault-Operation als Modellierungsoperation, die im Ablegen von Information aktiv ein Modell des eigenen Wissens formt.

Zwei Ebenen greifen dabei ineinander. Die Einheit dieses Modells ist das Wissensdokument, eine atomare, destillierte Wissensstruktur, die für Menschen lesbar und für Sprachmodelle als Kontext nutzbar ist. Die Dynamik des Modells sind die Wissenstransformationen, systematische Operationen, die Rohmaterial in solche Einheiten überführen. Beide zusammen machen den Vault zu einem externen Gedächtnis, dessen Output-Qualität von der Qualität seines Wissensmodells abhängt.

Dieses Dokument führt die Framing-Ebene (Vault als Modell), die Einheit (Wissensdokument) und die Operationen (Transformationen) zusammen, die zuvor in drei getrennten Atomen lagen.

## Der Vault als Wissensmodell

Die Struktur des Vaults ist bedeutungstragend. Ein gesetzter Link, ein gewählter Tag, eine Aufteilung eines Dokuments in kleinere Einheiten bestimmen, wie das enthaltene Wissen später interpretiert werden kann, durch einen menschlichen Leser ebenso wie durch ein Sprachmodell. Damit wird jede strukturelle Entscheidung zu einer epistemischen. Sie legt fest, welche Zusammenhänge sichtbar sind, welche Konzepte als eigenständig gelten und wie sich das Netz beim selektiven Laden in einen Kontext verhält.

Aus dieser Sicht folgen drei Implikationen für die Praxis. Für die Vault-Pflege gilt, dass strukturelle Arbeit Modellierungsarbeit ist und nicht bloße Ablage. Für die LLM-Nutzung wird der Vault zum externen Gedächtnis, das sich gezielt in Kontexte laden lässt, wobei die Güte des Modells die Güte des Outputs begrenzt. Für die Wissenserzeugung entsteht Neues vor allem durch die Transformationen, die weiter unten beschrieben sind.

Offen bleibt die Kalibrierung zwischen den beiden Leserichtungen. Ein Wissensmodell für LLM-Kontext und eines für menschliches Lesen können unterschiedliche Granularität verlangen, und der mögliche Zielkonflikt zwischen kompakter Maschinenlesbarkeit und ausführlicher menschlicher Nachvollziehbarkeit ist nicht abschließend geklärt. Ebenso offen ist, woran sich die Qualität eines Wissensmodells überhaupt messen lässt.

## Das Wissensdokument als Einheit

Ein Wissensdokument ist eine atomare, strukturierte Wissenseinheit, die durch Destillation aus Rohmaterial entsteht (Quellen, Erfahrungen, Daten) und als Kontextartefakt für die Zusammenarbeit zwischen Menschen und Sprachmodellen optimiert ist. Im Context Engineering fungiert es als materialisierte Context Compression, als vorab geleistete Verdichtung, die ein Modell nicht mehr selbst aus dem Rohmaterial rekonstruieren muss.

Das Format ruht auf mehreren Eigenschaften zugleich. Es ist dual lesbar, für Menschen verständlich und für LLMs als Kontext nutzbar. Es ist kompakt, mit maximaler Information bei minimalem Token-Aufwand. Und es ist portabel, als Markdown-Datei in Wissenssystemen wie Obsidian verwendbar, verlinkbar und austauschbar.

Ein gutes Wissensdokument ist zugleich transferierbar, kompakt und abrufbar. Transferierbarkeit heißt, dass das Wissen auf neue Situationen anwendbar bleibt, die beim Schreiben noch nicht bekannt waren. Kompaktheit heißt, dass nur enthalten ist, was für die Anwendung nötig ist, ohne redundante Erklärungen oder Beispiele. Abrufbarkeit heißt, dass klare Überschriften, Metadaten und eine logische Gliederung das Wissen schnell wieder aktivierbar machen. Ein solches Dokument ist weder Lehrbuch noch Tutorial. Es setzt voraus, dass der Leser den Kontext bereits kennt oder sich erschließen kann, und liefert ihm das konzentrierte Prinzip.

Der Destillationsprozess folgt einer Stufenlogik. Am Anfang steht ein konkretes Beispiel, ein Fall, ein Video, ein Text, eine Erfahrung. Darauf folgt die Musterextraktion mit der Frage, was hier funktioniert und warum. Die Muster werden zu Prinzipien abstrahiert, die vom Einzelfall gelöst sind, und schließlich in eine speicherbare, wieder abrufbare Form verdichtet. Das Ergebnis ist unabhängig vom Ursprungsbeispiel anwendbar. Wer das Dokument liest, kann die Prinzipien auf ganz andere Kontexte übertragen, ohne das ursprüngliche Material je gesehen zu haben. Ein Wissensdokument speichert damit Denkwerkzeuge statt bloßer Fakten. Der Test für ein gelungenes Dokument ist einfach. Kann jemand, der nur das Dokument liest, das Prinzip auf einen neuen Fall anwenden, ohne Rückfragen zu stellen?

## Wissenstransformationen

Wissenstransformationen sind systematische Operationen, die Information in wiederverwendbare, kontextualisierte Wissensstrukturen überführen. Sie sind die Dynamik, mit der aus Rohmaterial die im vorigen Abschnitt beschriebenen Einheiten werden. Fünf Operationen tragen das Vorgehen.

| Operation | Input | Output | Informationsfluss |
|-----------|-------|--------|-------------------|
| **Kompression/Destillation** | Folien, Vorlesung, Paper | Atomares Wissensdokument | Reduktion auf Kernkonzepte |
| **Normalisierung** | Rohe Meeting-Notizen | Strukturiertes Projektdokument | Chaotisch zu Frontmatter plus Sektionen |
| **Anreicherung** | Sparse Notiz | Kontextualisiertes Dokument | Idee plus Web-Recherche zu vollständig |
| **Konsolidierung** | Mehrere Dokumente | Ein integriertes Dokument | Redundanz eliminieren |
| **Atomisierung** | Monolithisches Dokument | Verlinkte Konzept-Einheiten | Ein Konzept, ein Dokument |

Zwei Fälle aus der Vault-Praxis zeigen die Richtungen. Bei der Atomisierung wird eine monolithische Vorlesungsmitschrift, in der viele einzeln referenzierbare Konzepte vermischt liegen, in mehrere atomare Dokumente aufgeteilt (je ein Konzept, einzeln auffindbar und verlinkbar), während das Ausgangsdokument zum MOC wird, der auf sie verweist. Bei der Konsolidierung laufen mehrere Dokumente aus demselben Kurs mit redundanten Grundlagen und fragmentierter Darstellung zu einem umfassenden Dokument mit durchgehender Pipeline zusammen, in dem die Redundanz getilgt ist. Die beiden Operationen wirken gegenläufig, das eine zerlegt, das andere führt zusammen, und beide dienen demselben Ziel, der sauberen Zuordnung von einem Konzept zu einer Einheit.

Vier Design-Prinzipien leiten die Transformationen. Das Atomic Principle hält fest, dass ein Konzept genau ein Dokument bewohnt und dass Vorlesungen und Kurse Quellen sind, die atomisiert werden. Self-Containedness verlangt, dass jedes Dokument für sich allein verständlich bleibt, mit dem nötigen Kontext im Dokument selbst und nicht nur in Verlinkungen, was für die LLM-Kontext-Nutzung entscheidend ist. Informationsdichte fordert maximale Information pro Token, ohne Füllwörter und ohne Redundanz zwischen Dokumenten. Provenance sichert die Herkunft über eine Sources-Sektion und Frontmatter mit `created`, `source` und `status`.

Für die Nutzung als LLM-Kontext gelten eigene Qualitätskriterien.

| Kriterium | Gut | Schlecht |
|-----------|-----|----------|
| Länge | mittlerer Umfang, weder Stub noch monolithisch | zu knapp (Stub) oder zu ausufernd (monolithisch) |
| Struktur | Frontmatter plus Sektionen plus Sources | Fließtext ohne Gliederung |
| Kontext | selbsterklärend | setzt andere Dokumente voraus |
| Redundanz | keine Duplikate | gleicher Inhalt in mehreren Files |

Der Arbeitsablauf mit LLM-Assistenz führt vom identifizierten Input über die Wahl der passenden Transformation und die assistierte Umsetzung im Vault-Format zur Integration (Links zu verwandten Konzepten, Eintrag in die relevanten MOCs) und zur abschließenden Validierung, ob das Dokument self-contained ist und genügend Substanz trägt.

## Theoretische Verankerung der Transformationen

Die fünf Operationen sind je einzeln in Traditionen der Informations- und Dokumentationswissenschaft sowie des Knowledge Management verankert (Verifikation der Anker 2026-07-23, webgestützte Literaturprüfung).

- Kompression/Destillation entspricht dem Referieren/Abstracting der Dokumentationswissenschaft, als Theorie und Technik kodifiziert bei Borko/Bernier (1975) und als Verfahren normiert in ISO 214:1976. Verdichtung ist damit ein standardisiertes Verfahren mit Regelwerk.
- Normalisierung entspricht der Formalerschließung, der formalen Beschreibung nach Regelwerk; konzeptuell integriert bei Svenonius (2000) unter dem Begriff der bibliographic languages, terminologisch im deutschsprachigen Bibliothekswesen bei Gantert (2016).
- Anreicherung entspricht der Sacherschließung und semantischen Erschließung, der inhaltlichen Beschreibung und Kontextualisierung (Svenonius 2000).
- Konsolidierung entspricht der Information Consolidation bei Saracevic/Wood (1981), die restructuring (Gehalt) von repackaging (Form) trennen, sowie der Kombination im SECI-Modell (Nonaka/Takeuchi 1995), explizites Wissen wird neu zusammengeführt.
- Atomisierung entspricht Otlets monographischem Prinzip (Traité de documentation, 1934), Wissen in kleinste, aus dem Dokumentverband gelöste, rekombinier- und neu klassifizierbare Einheiten zu zerlegen, und Luhmanns Zettelkasten-Praxis (1981) mit atomaren, fest adressierten, quervernetzten Notizeinheiten.

Die Elizitation als zweite Wissensquelle (implizites Expertenwissen heben) entspricht der Externalisierung im SECI-Modell; SECI ist ein Wissensschöpfungszyklus auf Organisationsebene, die Zuordnung auf Dokumentoperationen ist eine Übertragung. Das Provenance-Prinzip hat seine maschinenlesbare Form in W3C PROV (Recommendation 2013, Entity/Activity/Agent, wasDerivedFrom) und seine forschungspraktische Forderung in den FAIR-Prinzipien (Wilkinson et al. 2016, R1.2 detailed provenance). Der Gesamtvorgang, Wissen in ablegbare und wiederauffindbare Dokumente zu fassen, ist die knowledge codification des Knowledge Management (Davenport/Prusak 1998; Markus 2001 mit dem Stufenmodell capturing, packaging, reusing).

Eine kanonische Taxonomie von Dokumenttransformationen existiert in beiden Disziplinen nicht; Alavi/Leidner (2001) klassifizieren Wissensprozesse (creation, storage/retrieval, transfer, application), was quer zu den Dokumentoperationen liegt. Die Fünfer-Systematik ist daher eine eigene Prägung. Sie lässt sich als facettierte Klassifikation über zwei Achsen herleiten, als eigene Inferenz markiert: An den Einheitsgrenzen lässt sich zerlegen (Atomisierung) oder zusammenführen (Konsolidierung); an der Einheit selbst lässt sich der Gehalt reduzieren (Destillation) oder erweitern (Anreicherung) oder die Form bei konstantem Gehalt umordnen (Normalisierung). Die Gehalt-Form-Trennung folgt der Vorlage restructuring/repackaging bei Saracevic/Wood. Die Vollständigkeit gilt bei gegebener Achsendefinition; zusammengesetzte Vorgänge sind Kompositionen der Basisoperationen.

Quellen der Verankerung: Borko, H./Bernier, C. L. (1975). Abstracting Concepts and Methods. Academic Press. ISO 214:1976. Documentation — Abstracts for publications and documentation. Svenonius, E. (2000). The Intellectual Foundation of Information Organization. MIT Press. Gantert, K. (2016). Bibliothekarisches Grundwissen. 9. Aufl. De Gruyter Saur. Saracevic, T./Wood, J. B. (1981). Consolidation of Information. UNESCO PGI-81/WS/16. Nonaka, I./Takeuchi, H. (1995). The Knowledge-Creating Company. Oxford University Press. Otlet, P. (1934). Traité de documentation. Mundaneum. Luhmann, N. (1981). Kommunikation mit Zettelkästen. In: Baier, H. et al. (Hrsg.). Öffentliche Meinung und sozialer Wandel. Westdeutscher Verlag (Seitenangabe 222–228 vor Zitation prüfen). Davenport, T. H./Prusak, L. (1998). Working Knowledge. Harvard Business School Press. Markus, M. L. (2001). Toward a Theory of Knowledge Reuse. JMIS 18(1). Alavi, M./Leidner, D. E. (2001). MIS Quarterly 25(1), https://doi.org/10.2307/3250961. W3C (2013). PROV-O. Recommendation 30.04.2013. Wilkinson, M. D. et al. (2016). The FAIR Guiding Principles. Scientific Data 3, 160018, https://doi.org/10.1038/sdata.2016.18.

## Related

- [[Semantic Markdown]] — strukturierte Dokumentformate für LLMs
- [[Sparse Priming Representations (SPR)]] — komprimierte Wissensrepräsentation
- [[Context Window und Context Rot]] — Grenzen des LLM-Kontexts
- [[CLAUDE]] — Vault-Konventionen
- [[HOME|Vault-Struktur]] — Navigationshub
- [[Applied-GenerativeAI MOC]] — Anwendungsbereich
