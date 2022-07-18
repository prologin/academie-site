import { useState } from "react";
import { Box } from "@mui/material";

import AceEditor from "react-ace";

import "ace-builds/src-noconflict/mode-python";
import "ace-builds/src-noconflict/snippets/python";
import DropMenu from "./Menu";
const languages = ["python", "c_cpp", "javascript", "java", "golang", "csharp"];

const themes = [
  "monokai",
  "github",
  "tomorrow",
  "kuroir",
  "twilight",
  "xcode",
  "textmate",
  "solarized_dark",
  "solarized_light",
  "terminal",
];

languages.forEach((lang) => {
  require(`ace-builds/src-noconflict/mode-${lang}`);
  require(`ace-builds/src-noconflict/snippets/${lang}`);
});

themes.forEach((theme) => require(`ace-builds/src-noconflict/theme-${theme}`));

require("ace-builds/src-min-noconflict/ext-searchbox");
require("ace-builds/src-min-noconflict/ext-language_tools");

export default function Editor() {
  const [selectedLanguage, setSelectedLanguage] = useState("python");
  const [selectedTheme, setSelectedTheme] = useState("monokai");

  const [code, setCode] = useState("");

  return (
    <>
      <Box>
        <DropMenu
          values={languages}
          value={selectedLanguage}
          name="langage"
          onChange={setSelectedLanguage}
        />
        <DropMenu
          values={themes}
          value={selectedTheme}
          name="theme"
          onChange={setSelectedTheme}
        />
      </Box>
      <AceEditor
        width="100%"
        height="calc(100vh - 64px - 37px)"
        mode={selectedLanguage}
        theme={selectedTheme}
        fontSize={16}
        showPrintMargin={true}
        showGutter={true}
        highlightActiveLine={true}
        value={code}
        onChange={setCode}
        setOptions={{
          enableBasicAutocompletion: true,
          enableLiveAutocompletion: true,
          enableSnippets: false,
          showLineNumbers: true,
          tabSize: 2,
        }}
      />
    </>
  );
}
