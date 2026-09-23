// Offline execution of the pure Code-node bodies, not a live n8n import.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const workflow = JSON.parse(fs.readFileSync(path.join(__dirname, '../ai-ecommerce-news-workflow.json')));
const [sampleNode, formatNode] = workflow.nodes.filter(n => n.type === 'n8n-nodes-base.code');
const fixture = new Function(sampleNode.parameters.jsCode)();
const format = rows => new Function('$input', formatNode.parameters.jsCode)({all: () => rows});
const result = format(fixture)[0].json;
assert.equal(result.article_count, 2);
assert.equal(result.status, 'draft_requires_review');
assert.equal(format([])[0].json.article_count, 0);
assert.equal(format([{json: {title:'Missing link'}}])[0].json.skipped_invalid, 1);
assert.equal(format([{json: {title:'Bad', link:'javascript:alert(1)'}}])[0].json.article_count, 0);
assert.equal(format(Array.from({length: 30}, (_, i) => ({json:{title:`Item ${i}`,link:`https://example.com/${i}`}})))[0].json.article_count, 20);
assert.equal(workflow.active, false);
assert(!workflow.nodes.some(n => /httpRequest|telegram|scheduleTrigger/.test(n.type)));
console.log('PASS: workflow fixture, duplicates, empty input, invalid links, cap, no external actions');
