function cleanGadget(gadget) {
    // Map function names to symbol names + number
    const funSymbols = {};
    // Map variable names to symbol names + number
    const varSymbols = {};

    let funCount = 1;
    let varCount = 1;

    // Regular expression to catch multi-line comment
    const rxComment = /\*\/\s*$/;
    // Regular expression to find function name candidates
    const rxFun = /\b([_$a-zA-Z]\w*)\b(?=\s*\()/;
    // Regular expression to find variable name candidates
    const rxVar = /\b([_$a-zA-Z]\w*)\b(?:(?=\s*\w+\()|(?!\s*\w+))(?!\s*\()/;

    // Final cleaned gadget output to return
    const cleanedGadget = [];

    gadget.forEach(line => {
        // Process if not a multi-line commented line
        if (!rxComment.test(line)) {
            // Remove all string literals (keep the quotes)
            let noStrLitLine = line.replace(/".*?"/g, '""');
            // Remove all character literals
            let noCharLitLine = noStrLitLine.replace(/'.*?'/g, "''");
            // Replace any non-ASCII characters with empty string
            const asciiLine = noCharLitLine.replace(/[^\x00-\x7f]/g, '');

            // Find function names in the line
            const userFun = asciiLine.match(rxFun);
            // Find variable names in the line
            const userVar = asciiLine.match(rxVar);

            // Process function names
            userFun.forEach(funName => {
                // Check if function name is not a reserved keyword
                if (!reservedKeywords.includes(funName)) {
                    // Check if function name already exists in dictionary
                    if (!funSymbols[funName]) {
                        funSymbols[funName] = 'FUN' + funCount;
                        funCount++;
                    }
                    // Replace function name with symbol name
                    asciiLine = asciiLine.replace(new RegExp('\\b' + funName + '\\b(?=\\s*\\()', 'g'), funSymbols[funName]);
                }
            });

            // Process variable names
            userVar.forEach(varName => {
                // Check if variable name is not a reserved keyword
                if (!reservedKeywords.includes(varName)) {
                    // Check if variable name already exists in dictionary
                    if (!varSymbols[varName]) {
                        varSymbols[varName] = 'VAR' + varCount;
                        varCount++;
                    }
                    // Replace variable name with symbol name
                    asciiLine = asciiLine.replace(new RegExp('\\b' + varName + '\\b(?:(?=\\s*\\w+\\()|(?!\s*\\w+))(?!\\s*\\()', 'g'), varSymbols[varName]);
                }
            });

            // Append the modified line to the cleaned gadget
            cleanedGadget.push(asciiLine);
        }
    });

    return cleanedGadget;
}

// Reserved keywords in JavaScript/TypeScript
const reservedKeywords = [
    'abstract', 'await', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 'const', 'continue', 'debugger',
    'default', 'delete', 'do', 'double', 'else', 'enum', 'export', 'extends', 'false', 'final', 'finally', 'float',
    'for', 'function', 'goto', 'if', 'implements', 'import', 'in', 'instanceof', 'int', 'interface', 'let', 'long',
    'native', 'new', 'null', 'package', 'private', 'protected', 'public', 'return', 'short', 'static', 'super',
    'switch', 'synchronized', 'this', 'throw', 'throws', 'transient', 'true', 'try', 'typeof', 'var', 'void',
    'volatile', 'while', 'with', 'yield'
];

// Example usage:
const codeLines = [
    'function add(a, b) { return a + b; }',
    'let x = 10;',
    'for (let i = 0; i < 10; i++) { console.log(i); }'
];

const cleanedCode = cleanGadget(codeLines);
console.log(cleanedCode);
