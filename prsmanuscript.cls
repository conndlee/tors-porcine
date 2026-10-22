%% Unofficial PRS manuscript class. Submission is default; journalpreview
%% is for visual drafting ONLY, not publisher-accurate and not for upload.
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{prsmanuscript}[2026/10/13 PRS submission + journal-style preview]
\newif\ifprs@preview
\newif\ifprs@draftfigures
\prs@previewfalse\prs@draftfiguresfalse
\DeclareOption{journalpreview}{\prs@previewtrue}
\DeclareOption{submission}{\prs@previewfalse}
\DeclareOption{draftfigures}{\prs@draftfigurestrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\ifprs@preview\LoadClass[10pt,letterpaper]{article}\else\LoadClass[12pt,letterpaper]{article}\fi
\RequirePackage[T1]{fontenc}
\RequirePackage{newtxtext,newtxmath}
\RequirePackage{geometry}
\RequirePackage{setspace}
\RequirePackage{graphicx,booktabs,tabularx,array,threeparttable}
\RequirePackage{amsmath}
\RequirePackage{siunitx}
\RequirePackage{caption}
\RequirePackage{fancyhdr}
\RequirePackage{xcolor}
\RequirePackage{lineno}
\RequirePackage{url}
\RequirePackage[hidelinks]{hyperref}
\RequirePackage{xparse}
\ifprs@preview
  \geometry{margin=.72in,columnsep=.26in}
  \setstretch{1.02}
  % Allow long drafting placeholders and references to wrap in narrow columns.
  \setlength{\emergencystretch}{2em}
  \setlength{\parindent}{1em}
  \setlength{\parskip}{0pt}
  \captionsetup{font=footnotesize,labelfont=bf,labelsep=period}
  \renewcommand\thesection{}\renewcommand\thesubsection{}
  \renewcommand\section{\@startsection{section}{1}{\z@}{1.3ex plus .4ex}{.55ex}{\normalfont\normalsize\bfseries}}
  \renewcommand\subsection{\@startsection{subsection}{2}{\z@}{1.1ex plus .2ex}{.3ex}{\normalfont\small\bfseries\itshape}}
  \pagestyle{fancy}\fancyhf{}\fancyhead[L]{\footnotesize PLASTIC AND RECONSTRUCTIVE SURGERY}\fancyhead[R]{\footnotesize Manuscript Preview}\fancyfoot[C]{\thepage}
  \setlength{\headheight}{15pt}
\else
  \geometry{margin=1in}
  \doublespacing
  \setlength{\parindent}{1.5em}
  \setlength{\parskip}{0pt}
  \captionsetup{font=normalsize,labelfont=bf,labelsep=period}
  \renewcommand\thesection{}\renewcommand\thesubsection{}
  \renewcommand\section{\@startsection{section}{1}{\z@}{-2.8ex plus -.8ex}{1.2ex}{\normalfont\normalsize\bfseries}}
  \renewcommand\subsection{\@startsection{subsection}{2}{\z@}{-2ex plus -.5ex}{.8ex}{\normalfont\normalsize\itshape}}
  \pagestyle{fancy}\fancyhf{}\fancyfoot[C]{\thepage}\renewcommand\headrulewidth{0pt}
  \setlength{\headheight}{14pt}
\fi
\newcommand\PRStitle[1]{\gdef\prs@title{#1}}
\newcommand\PRSauthors[1]{\gdef\prs@authors{#1}}
\newcommand\PRSaffiliations[1]{\gdef\prs@affiliations{#1}}
\newcommand\PRScorrespondence[1]{\gdef\prs@correspondence{#1}}
\newcommand\PRSshorttitle[1]{\gdef\prs@shorttitle{#1}}
\newcommand\PRSwordcounts[2]{\gdef\prs@abstractcount{#1}\gdef\prs@bodycount{#2}}
\newcommand\PRSmetadata[1]{\gdef\prs@metadata{#1}}
\def\prs@title{[Manuscript title]}\def\prs@authors{[Authors]}\def\prs@affiliations{[Affiliations]}
\def\prs@correspondence{[Correspondence]}\def\prs@shorttitle{[Running title]}
\def\prs@abstractcount{[verify]}\def\prs@bodycount{[verify]}\def\prs@metadata{}
% In preview mode, title and abstract are emitted together by \PRSstartbody
% as full-width material above the first page's two columns.
\newcommand\prs@previewtitle{%
 \begin{center}{\LARGE\bfseries\prs@title\par}\vspace{.75em}
 {\normalsize\prs@authors\par}\end{center}\vspace{.6em}}
\newcommand\PRSmaketitle{%
\ifprs@preview
 % Deferred until the abstract is available.
\else
 \begin{titlepage}\thispagestyle{empty}\begin{center}
 {\large\bfseries\prs@title\par}\vspace{1.8em}
 {\prs@authors\par}\vspace{1.2em}{\prs@affiliations\par}\end{center}\vspace{1.8em}
 \noindent\textbf{Running title:} \prs@shorttitle\par
 \noindent\textbf{Corresponding author:} \prs@correspondence\par
 \noindent\textbf{Abstract word count:} \prs@abstractcount\par
 \noindent\textbf{Main-text word count:} \prs@bodycount\par\medskip
 \prs@metadata\end{titlepage}\setcounter{page}{1}
\fi}
\def\prs@abstractbody{}
\NewDocumentEnvironment{PRSabstract}{+b}{%
\ifprs@preview
 \gdef\prs@abstractbody{#1}%
\else
 \clearpage\section*{Abstract}\begingroup #1\par\endgroup\clearpage
\fi
}{}
\newcommand\abstractpart[2]{\par\noindent\textbf{#1:} #2\par}
\newcommand\PRSkeywords[1]{\par\noindent\textbf{Keywords:} #1\par}
\newcommand\PRSstartbody{%
\ifprs@preview
 \twocolumn[{%
  \prs@previewtitle
  \par\noindent\textbf{Abstract}\par\smallskip
  \begingroup\small\prs@abstractbody\par\endgroup\vspace{.7em}%
 }]%
 % An unnumbered footnote keeps the affiliation block at the bottom of the
 % first column, with space reserved by LaTeX's normal page builder.
 \begingroup
  \renewcommand\thefootnote{}%
  \renewcommand\@makefntext[1]{\noindent##1}%
  \footnotetext{\prs@affiliations}%
 \endgroup
\fi}
\newcommand\PRSdisclosure[2]{\par\noindent\textbf{#1:} #2\par}
\newcommand\PRStable[2]{\par\refstepcounter{table}\label{#1}\noindent\textbf{Table \thetable.} #2\par\medskip}
\newcommand\PRSfigurelegend[2]{\par\noindent\textbf{Fig. #1.} #2\par\medskip}
\newcommand\PRSfigureplaceholder[2]{\ifprs@draftfigures\par\begin{center}\fbox{\parbox[c][1.25in][c]{.8\linewidth}{\centering\textbf{Draft figure #1}\par #2}}\end{center}\fi}
\AtBeginDocument{\ifprs@preview\else\linenumbers\fi}
\endinput
