-- Keep verification text red and flag any unconverted LaTeX rather than losing it.
function Span(span)
  if span.attributes.style == 'color: red' then
    span.attributes['custom-style'] = 'Verification'
  end
  return span
end

function RawInline(raw)
  if raw.format == 'latex' or raw.format == 'tex' then
    error('Unconverted LaTeX: ' .. raw.text)
  end
end

RawBlock = RawInline

local figure_number = 0
function Figure(figure)
  figure_number = figure_number + 1
  local caption = figure.caption.long[1]
  caption.content:insert(1, pandoc.Space())
  caption.content:insert(1, pandoc.Strong{pandoc.Str('Figure ' .. figure_number .. '.')})
  return figure
end
