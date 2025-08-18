bg = " "
fraction = "─"

special_symbols = {
    "~": " "
}
single_line_leaf_commands = {
    "LaTeX": "LᴬTₑX",
    "TeXtR": "TₑXᵀR",
    "mod": "  mod",

    "textit": " ", "oplus": "⊕", "otimes": "⊗", "ominus": "⊖",
    "leq": "≤", "equiv": "≡", "geq": "≥", "partial": "∂",
    "forall": "∀", "exists": "∃", "owns": "∋", "ni": "∌",
    "in": "∈", "notin": "∉", "qed": "∎", "pm": "±",
    "mp": "∓", "cong": "≅", "neq": "≠", "nmid": "∤",
    "subset": "⊂", "subseteq": "⊆", "supseteq": "⊇", "supset": "⊃",
    # "sqrt" : "radical",
    # "buildrel" : "buildrel",
    # "frac" : "fraction",
    # "LITERALnoLENGTH" : "literal_no_length",
    "alpha": "α", "Alpha": "Α", "beta": "β", "Beta": "Β", "gamma": "γ", "Gamma": "Γ",
    "delta": "δ", "Delta": "Δ", "epsilon": "ε", "Epsilon": "Ε", "zeta": "ζ", "Zeta": "Ζ",
    "eta": "η", "Eta": "Η", "theta": "θ", "Theta": "Θ", "iota": "ι", "Iota": "Ι",
    "phi": "φ", "Phi": "Φ", "kappa": "κ", "Kappa": "Κ", "lambda": "λ", "Lambda": "Λ",
    "mu": "μ", "Mu": "Μ", "nu": "ν", "Nu": "Ν", "xi": "ξ", "Xi": "Ξ",
    "omicron": "ο", "Omicron": "Ο", "pi": "π", "Pi": "Π", "rho": "ρ", "Rho": "Ρ",
    "sigma": "σ", "Sigma": "Σ", "tau": "τ", "Tau": "Τ", "upsilon": "υ", "Upsilon": "Υ",
    "chi": "χ", "Chi": "Χ", "psi": "ψ", "Psi": "Ψ", "omega": "ω", "Omega": "Ω",

    "~": " ", ",": " ", "dots": "...",
    "ldots": "...", "cdots": "⋯", "colon": ": ",
    "mid": " | ",
    "smallsetminus": " ⧵ ",
    "setminus": " ⧹ ",
    # "backslash"     : "\\" ,
    "approx": " ≅ ", "simeq": " ≃ ", "quad": "   ", "qquad": "     ",
    # "Delta"  : "△"    , "Pi"     : "π"    , "alpha"  : "α"    , "to"     : " ──> ",
    # "from"   : " <── ", "wedge"  : "∧"    , "Lambda" : "∨"    , "lhd"    : " ⊲ "  ,
    "rhd": " ⊳ ", "cdot": " · ", "circ": " o ", "bullet": "•",
    "infty": "∞", "ltimes": "⋉", "rtimes": " ⋊ ", "times": " × ",
    "hookrightarrow": " ↪ ", "hookleftarrow": " ↩ ",
    "longleftarrow": " <──── ", "longrightarrow": " ────> ",
    "longleftrightarrow": " <────> ",
    "rightarrow": " ──> ", "leftarrow": " <── ",
    "Rightarrow": " ==> ", "Leftarrow": " <== ",
    "mapsto": " ├──> ", "longmapsto": " ├────> ",
    "cap": " ∩ ", "cup": " ∪ ",
    "section": "Section ", "subsection": "Subsection ",
    "|": "||", ';': " ",
    # '\noindent'  : "",
}

multi_line_leaf_commands = {
    "sum":
    (["┌──",
      "🮥  ",
      "└──",],
     1),
    "prod":
    (["┰─┰",
      "┃ ┃",
      "┸ ┸",],
     1),
    "int":
    (["⌠",
      "⎮",
      "⌡",],
     1),
    "iint":
    (["⌠⌠",
      "⎮⎮",
      "⌡⌡",],
     1),
    "iiint":
    (["⌠⌠⌠",
      "⎮⎮⎮",
      "⌡⌡⌡",],
     1),
    "idotsint":
    (["⌠ ⌠",
      "⎮⋯⎮",
      "⌡ ⌡",],
     1),
    "oint":
    ([" ⌠ ",
      "❨⎮❩",
      " ⌡ ",],
     1),
    "oiint":
    ([" ⌠⌠ ",
      "❨⎮⎮❩",
      " ⌡⌡ ",],
     1),
    "oiiint":
    ([" ⌠⌠⌠ ",
      "❨⎮⎮⎮❩",
      " ⌡⌡⌡ ",],
     1),
}

square_root = {
    "top_bar": "─",
    "top_angle": bg + "┌",
    "left_bar":  bg + "│",
    "btm_angle":     "🯓🯗",
}

unicode_scripts = {
    " ": "  ", "0": "⁰₀", "1": "¹₁", "2": "²₂", "3": "³₃", "4": "⁴₄",
    "5": "⁵₅", "6": "⁶₆", "7": "⁷₇", "8": "⁸₈", "9": "⁹₉",
    "+": "⁺₊", "-": "⁻₋", "=": "⁼₌", "!": "ꜝ ", "(": "⁽₍", ")": "⁾₎",
    "A": "ᴬ ", "a": "ᵃₐ", "B": "ᴮ𞁓", "b": "ᵇ ", "C": "ᶜ𞁞", "c": "ᶜ𞁞",
    "D": "ᴰ ", "d": "ᵈ ", "E": "ᴱ ", "e": "ᵉₑ", "F": "ᶠ ", "f": "ᶠ ",
    "G": "ᴳ ", "g": "ᵍ ", "H": "ᴴ ", "h": "ʰₕ", "I": "ᴵᶦ", "i": "ⁱᵢ",
    "J": "ᴶ ", "j": "ʲⱼ", "K": "ᴷ𞁚", "k": "ᵏₖ", "L": "ᴸ ", "l": "ˡₗ",
    "M": "ᴹ ", "m": "ᵐₘ", "N": "ᴺ ", "n": "ⁿₙ", "O": "ᴼ𞁜", "o": "ᵒₒ",
    "P": "ᴾ ", "p": "ᵖₚ", "Q": "ꟴ ", "q": "𐞥 ", "R": "ᴿ ", "r": "ʳᵣ",
    "S": "ˢₛ", "s": "ˢₛ", "T": "ᵀ ", "t": "ᵗₜ", "U": "ᵁ ", "u": "ᵘᵤ",
    "V": "ⱽᵥ", "v": "ᵛᵥ", "W": "ᵂ ", "w": "ʷ ", "X": "ˣₓ", "x": "ˣₓ",
    "Y": "𐞲ᵧ", "y": "ʸᵧ", "Z": "ᶻ ", "z": "ᶻ ",
    "α": "ᵅ ", "β": "ᵝᵦ", "γ": "ᵞᵧ", "δ": "ᵟ ", "ε": "ᵋ ", "θ": "ᶿ ",
    "ι": "ᶥ ", "ϕ": "ᶲ ", "φ": "ᵠᵩ", "χ": "ᵡᵪ", "ρ": "ᵨ ",
}

delimiter = {
    "left":  {"sgl": "([{|",
              "top": "⎛⎡⎧⎟",
              "ctr": "⎜⎢⎨⎟",
              "fil": "⎜⎢⎪⎟",
              "btm": "⎝⎣⎩⎟"},
    "right": {"sgl": ")]}|",
              "top": "⎞⎤⎫⎜",
              "ctr": "⎟⎥⎬⎜",
              "fil": "⎟⎥⎪⎜",
              "btm": "⎠⎦⎭⎜"},
}
