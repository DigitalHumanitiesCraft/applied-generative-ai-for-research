/* Reading view conveniences. The pages are complete without this script: both
   language routes stand open on the landing page and every link is a plain link.
   The script adds one thing, a remembered language route.

   Storage is wrapped, because a browser that blocks site data throws on access
   rather than returning null. */

const KEY = "agai-reading-language";
const LANGUAGES = ["en", "de"];
const LABEL = { en: "English", de: "Deutsch" };

function readLanguage() {
  try {
    const stored = localStorage.getItem(KEY);
    return LANGUAGES.includes(stored) ? stored : null;
  } catch (error) {
    return null;
  }
}

function writeLanguage(language) {
  try {
    localStorage.setItem(KEY, language);
  } catch (error) {
    /* A reader without site data keeps the default view. */
  }
}

function setUpLanding() {
  const filter = document.getElementById("route-filter");
  const routes = Array.from(document.querySelectorAll(".route[data-lang]"));
  if (!filter || routes.length < 2) return;

  const buttons = new Map();

  function apply(language) {
    routes.forEach((route) => {
      route.hidden = route.dataset.lang !== language;
    });
    buttons.forEach((button, code) => {
      button.setAttribute("aria-pressed", String(code === language));
    });
  }

  routes.forEach((route) => {
    const code = route.dataset.lang;
    const button = document.createElement("button");
    button.type = "button";
    button.lang = code;
    button.textContent = LABEL[code] || code;
    button.setAttribute("aria-pressed", "false");
    button.addEventListener("click", () => {
      writeLanguage(code);
      apply(code);
    });
    buttons.set(code, button);
    filter.appendChild(button);
  });

  filter.hidden = false;
  apply(readLanguage() || routes[0].dataset.lang);
}

function setUpChapter() {
  /* The chapter a reader has open is the route the landing page should offer next. */
  const article = document.querySelector(".chapter[lang]");
  if (article && LANGUAGES.includes(article.lang)) writeLanguage(article.lang);
}

setUpLanding();
setUpChapter();
