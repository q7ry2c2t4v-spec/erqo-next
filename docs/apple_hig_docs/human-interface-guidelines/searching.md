# 検索

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/searching

# 検索

ユーザは、デバイス上、アプリ内、書類やファイル内のコンテンツを見つけるために、さまざまな方法で検索します。

![拡大鏡のスケッチ。情報の検索を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせるオレンジ色になっています。](https://docs-assets.developer.apple.com/published/031471cf2ae3b666268d16f96cbce4e9/patterns-searching-intro%402x.png)

アプリ内のコンテンツを検索する場合は、通常、[検索フィールド](/jp/design/human-interface-guidelines/search-fields)が使用されます。アプリによっては、ユーザがどのようにアプリを操作するかについて分かっていることから検索体験をパーソナライズできます。例えば、最近の検索結果を表示したり、ユーザが以前にアプリ内で検索した語句に基づいて、検索候補、補完、修正を提供したりできます。

場合によっては、検索範囲を指定する機能や検索結果を絞り込む機能がユーザに喜ばれます。例えば、作成日、ファイルサイズ、ファイルタイプのような属性を指定して語句を検索できます。ガイダンスは[スコープコントロールとトークン](/jp/design/human-interface-guidelines/search-fields#Scope-controls-and-tokens)を参照してください。また、iOSアプリ、iPadOSアプリ、またはmacOSアプリで、ウインドウまたはページ内のコンテンツを検索する方法を組み込むと、ユーザが開いた書類やファイル内のコンテンツを検索できるようになります。

iOS、iPadOS、macOSでは、Spotlightを使用してシステム内のすべてのアプリおよびWeb上のコンテンツを検索できます。アプリのコンテンツのインデックスを作成してコンテンツの情報を提供すると、ユーザはアプリを開かずにSpotlightを使用してアプリに含まれるコンテンツを検索できるようになります。ガイダンスは、[システム全体の検索](/jp/design/human-interface-guidelines/searching#Systemwide-search)を参照してください。

## [ベストプラクティス](/jp/design/human-interface-guidelines/searching#Best-practices)

**検索が重要な場合は、プライマリアクションにすることを検討する。** 例えば、iOSのApple TV、写真、電話アプリでは、検索は独立したタブとして[タブバー](/jp/design/human-interface-guidelines/tab-bars)に表示されます。メモアプリでは、検索フィールドが[ツールバー](/jp/design/human-interface-guidelines/toolbars)にあり、検索が明確に表示され、簡単にアクセスできます。

**1か所からアプリのコンテンツを検索できるように心がける。** アプリ内で探しているものすべてが、明確に識別できる1か所で見つけられるとユーザに喜ばれます。セクションが明確に区切られているアプリでも、ローカル検索機能を提供すると便利です。例えば、iOSの電話アプリで「履歴」や「連絡先」を検索すると、現在のビューがフィルタとして機能します。

**プレースホルダテキストを使用して、検索可能なコンテンツを示します。** 例えば、TVアプリには「 _番組、映画、その他_ 」というプレースホルダテキストが含まれます。

**検索の現在の範囲を明確に表示する。** 説明的なプレースホルダテキスト、[スコープコントロール](/jp/design/human-interface-guidelines/search-fields#Scope-controls-and-tokens)、またはタイトルを使用して、ユーザが現在検索している内容を強調します。例えば、メールアプリでは、ユーザが検索しているメールボックスが常に明確に表示されます。

**検索候補を提示して簡単に検索できるようにする。** 入力前および入力中に最近の検索結果や提案を表示することで、ユーザは素早く検索でき、入力を減らすことができます。デベロッパ向けのガイダンスは、[`searchSuggestions(_:)`](/documentation/SwiftUI/View/searchSuggestions\(_:\))を参照してください。

**検索履歴を表示する前にプライバシーに配慮する。** 他人に見られるかもしれない場所で自分の検索履歴が表示されるのを好まないユーザもいます。状況に応じて、検索を絞り込む他の方法を用意することを検討してください。検索履歴を表示する場合は、ユーザが適宜履歴を消去できる方法を用意します。

## [システム全体の検索](/jp/design/human-interface-guidelines/searching#Systemwide-search)

**Spotlightでアプリのコンテンツを検索できるようにする。** コンテンツをSpotlightに共有するには、コンテンツのインデックスを作成できるようにして、 _メタデータ_ と呼ばれる記述属性を指定します。Spotlightでは、この情報を抽出、保存、分類して、包括的な高速検索が行われます。

**アプリで処理するカスタムファイルタイプのメタデータを定義する。** 使用するファイルフォーマットに含まれるメタデータのタイプを記述するSpotlight File Importerプラグインを用意します。デベロッパ向けのガイダンスは、[`CSImportExtension`](/documentation/CoreSpotlight/CSImportExtension)を参照してください。

**アプリのコンテキスト内でSpotlightを使用して高度なファイル検索機能を提供する。** 例えば、現在の選択に基づいてSpotlight検索をすぐに始めるボタンを含めることができます。検索の実行後は、検索結果やそのフィルタ済みサブセットが含まれるカスタムビューを表示できます。

**システムで提供される開く/保存ビューを優先して使用する。** システム提供の開く/保存ビューには、通常、ユーザがシステム全体を検索して絞り込むために使用できる検索フィールドが組み込まれています。関連するガイダンスは、[ファイルの管理](/jp/design/human-interface-guidelines/file-management)を参照してください。

**アプリでカスタムファイルタイプを作成する場合は、Quick Lookジェネレータを実装する。** Quick Lookジェネレータを実装すると、Spotlightやその他のアプリで書類のプレビューを表示できるようになります。デベロッパ向けのガイダンスは、[Quick Look](/documentation/QuickLook)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/searching#Platform-considerations)

 _iOS、iPadOS、macOS、tvOS、visionOS、watchOSに追加の考慮事項はありません。_

## [リソース](/jp/design/human-interface-guidelines/searching#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/searching#Related)

[検索フィールド](/jp/design/human-interface-guidelines/search-fields)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/searching#Developer-documentation)

[アプリのコンテンツをSpotlightのインデックスに追加する](/documentation/CoreSpotlight/adding-your-app-s-content-to-spotlight-indexes) — Core Spotlight

#### [ビデオ](/jp/design/human-interface-guidelines/searching#Videos)

[](https://developer.apple.com/videos/play/wwdc2024/10131)

[](https://developer.apple.com/videos/play/wwdc2022/10009)

[](https://developer.apple.com/videos/play/wwdc2021/10176)

## [変更履歴](/jp/design/human-interface-guidelines/searching#Change-log)

日付| 変更内容  
---|---  
2025年6月09日| 検索フィールドの一般的なガイダンスでベストプラクティスを更新、およびシステム全体の検索に関するガイダンスを再編成。
