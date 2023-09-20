import Reveal from 'reveal.js';

// Plugins
import Markdown from 'reveal.js/plugin/markdown/markdown.esm.js';
import Notes from 'reveal.js/plugin/notes/notes.esm.js';
import Highlight from 'reveal.js/plugin/highlight/highlight.esm.js';

// CSS
import 'reveal.js/dist/reveal.css'
// see available themes in the
// node_modules/reveal.js/dist/theme
//  beige, black, blood, league, moon, night, serif, simple, ...
// import 'reveal.js/dist/theme/black.css'
import 'reveal.js/dist/theme/solarized.css'

let deck = new Reveal({
   plugins: [ Markdown, Notes, Highlight ]
})

export default deck;
