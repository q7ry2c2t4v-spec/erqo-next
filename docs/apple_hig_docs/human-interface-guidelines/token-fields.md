# トークンフィールド

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/token-fields

# トークンフィールド

トークンフィールドは、テキストを _トークン_ に変換できるテキストフィールドの一種です。トークンにすると、テキストを容易に選択したり操作したりできます。

![図案化されたテキストフィールド。トークンとしてフォーマットされた人名が含まれています。画像は全体が、6色のオリジナルAppleロゴを連想させる赤色になっています。](https://docs-assets.developer.apple.com/published/52b0ce3b39191294b47b0cd06198e5db/components-token-field-intro%402x.png)

例えば「メール」では、作成ウインドウのアドレスフィールドにトークンフィールドが使用されています。ユーザが宛先を入力すると、各宛先の名前を表すテキストがトークンに変換されます。これらの宛先トークンは選択したりドラッグして並べ替えたりすることが可能で、別のフィールドに移動させることもできます。

トークンフィールドは、フィールドへのテキスト入力中に候補リストが表示されるように設定できます。例えば「メール」では、アドレス欄への入力中に宛先の候補が表示されます。ユーザが宛先の候補を選択すると、その宛先がトークンとしてアドレス欄に挿入されます。

![「メール」のメール作成ウインドウの一部。トークンで宛先の候補が表示されています。](https://docs-assets.developer.apple.com/published/fb376529b5420a77a8d3483422ed8e9f/token-fields-suggestion%402x.png)

各トークンに、トークンについての情報または編集オプションを提供するコンテキストメニューを含めることもできます。例えば、「メール」の宛先トークンのコンテキストメニューには、宛先の名前を編集するコマンド、宛先をVIPに追加するコマンド、宛先の連絡先カードを表示するコマンドなどが含まれます。

![「メール」のメール作成ウインドウの一部。1つの宛先トークンのコマンドメニューが表示されています。](https://docs-assets.developer.apple.com/published/dfb348c9a3cf3bd23eb3886dff7e7e4c/token-fields-contextual%402x.png)

状況によっては、トークンを検索語句として使うこともできます。ガイダンスは、[検索フィールド](/jp/design/human-interface-guidelines/search-fields)を参照してください。

## [ベストプラクティス](/jp/design/human-interface-guidelines/token-fields#Best-practices)

**コンテキストメニューで利便性を高める。** トークンに関する追加のオプションや情報を含む[コンテキストメニュー](https://developer.apple.com/jp/design/human-interface-guidelines/context-menus)は、ユーザにとって便利な機能です。

**テキストをトークンに変換する方法を増やす。** デフォルトでは、テキストに続いてカンマを入力するとトークンに変換されます。これと同じアクションを実行するショートカット（例えばReturnキーを押す）を追加で指定できます。

**トークンの候補が表示されるまでのシステムの遅延時間をカスタマイズする。** デフォルトでは候補はすぐに表示されますが、候補の表示が早すぎると入力の妨げになることもあります。アプリでトークンの候補を表示するようにしている場合は、ユーザが快適に使えるように遅延時間を調整できます。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/token-fields#Platform-considerations)

 _iOS、iPadOS、tvOS、visionOS、watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/token-fields#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/token-fields#Related)

[テキストフィールド](/jp/design/human-interface-guidelines/text-fields)

[検索フィールド](/jp/design/human-interface-guidelines/search-fields)

[コンテキストメニュー](/jp/design/human-interface-guidelines/context-menus)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/token-fields#Developer-documentation)

[`NSTokenField`](/documentation/AppKit/NSTokenField) — AppKit
