# Histórico de desenvolvimento

## 0.5.5 — 11 de novembro de 2026 — experimental

Correção editorial, sem mudança de método e sem novos ensaios.

- Remove do protocolo as referências a “esta conversa” e a afirmação de que a consolidação não constitui publicação no GitHub.
- Acrescenta ao cabeçalho de distribuição a salvaguarda sobre `exemplos/` e `avaliacao/` e a ordem de entrega do módulo 2 (parecer breve primeiro, anexo compacto depois).
- Regenera `SHA256SUMS.txt`, que estava em desacordo com `SKILL.md`, `README.md` e `CHANGELOG.md` desde a padronização de 10 de novembro de 2026.
- Acrescenta `.gitattributes` com finais de linha LF, para que a conferência de hashes não falhe em clones feitos no Windows.
- `verificar_integridade.py` ignora linhas vazias do manifesto e confere se o corpo de `SKILL.md` coincide com `protocolo.md`.

## 0.5.4 — 5 de novembro de 2026 — experimental

[Commit da publicação](https://github.com/itamarfreitasufs-arch/-jason-perguntas-historicas/commit/7796814c682c0ea400b258f0e7f6ed87add1c383).

- Distingue inferioridade comparativa de declínio temporal; exige referente antes de inferir direção.
- Separa identificação de desacordo e escolha da afirmação verdadeira; contagem de ocorrências não determina reparo histórico.
- Explicita materiais congelados, leituras adicionais, contexto compartilhado e origem dos hashes.
- Atualiza instruções públicas, exemplos fictícios e limites da avaliação. Não altera retroativamente as saídas e os resultados da 0.5.3.

## 0.5.3 — desenvolvimento anterior à publicação

- Controle de escrita, publicação e reedição como acontecimentos diferentes.
- Dependências de secundárias condicionadas à central e ao nível de demanda.
- Registros de leitura e integridade mais explícitos.
- Ensaios documentais e controlados descritos em AVALIACAO.md.

Versões de desenvolvimento anteriores não são anunciadas como publicações prévias no GitHub. As próximas correções devem preservar a identificação das versões e descrever mudanças e limites.

## Convenção de versões

Cada skill segue sua própria sequência `principal.secundária.correção`. Incremente o último número para correções pontuais e o número do meio para mudanças relevantes no método, reiniciando o último em zero. Registre o estágio da edição em separado, como experimental, em validação ou estável. Reserve `1.0.0` para a primeira edição que cumpra critérios explícitos de validação.

Registre cada mudança coerente em um commit. Para cada marco de versão, anote o commit correspondente, as mudanças, os testes realizados e as pendências.
