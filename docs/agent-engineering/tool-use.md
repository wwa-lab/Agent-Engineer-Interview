# Tool Use

Tools turn model intent into effects. Design them as small APIs with typed inputs, bounded outputs, explicit identity, authorization, timeout, retry class, and audit behavior. Read tools and write tools should be distinct. Treat every result as untrusted data and make mutations previewable or reversible where possible.
