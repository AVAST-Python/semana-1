import reveal from './reveal.js'

async function getMarkdown(file) {
  const response = await fetch(`${file}`);
  return response.text();
}

async function substituteMarkdown(external) {
  console.log(external)
  const file = external.getAttribute('data-file-markdown')
  const markdown = await getMarkdown(file)
  console.log(markdown)
  external.outerHTML = `
    <section data-markdown>
      <textarea data-template>
        ${markdown}
      </textarea>
    </section>
  `
}

async function initialize() {
  const externals = document.querySelectorAll('section[data-file-markdown]')

  const substitutions = Array.from(externals).map(
      external => substituteMarkdown(external)
  )
  await Promise.all(substitutions)

  // We must initialize reveal.js once the markdown has been substituted
  reveal.initialize()
}

initialize()
