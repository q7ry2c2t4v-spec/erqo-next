# アウトラインビュー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/outline-views

# アウトラインビュー

アウトラインビューは、列と行に整理されるセルのスクロールするリストで、階層型のデータの表示に適しています。

![図案化されたフォルダと画像のリスト。「名前」、「変更日」、「サイズ」、および「種類」の4列を含むアウトラインビューです。画像全体が、6色の初代Appleロゴの赤色を連想させる赤みを帯びています。](https://docs-assets.developer.apple.com/published/86254b48c28f688cdbc0e42d4e24a955/components-outline-view-intro%402x.png)

アウトラインビューには、親コンテナとその子の集合のような、階層型のプライマリデータを含む列が少なくとも1つ存在します。必要に応じて列を追加し、プライマリデータを補足するサイズや変更日などの属性を表示できます。親コンテナにある開閉用三角ボタンを押すと、展開して子を表示できます。

Finderのウインドウは、ファイルシステム内の移動用にアウトラインビューを提供しています。

## [ベストプラクティス](/jp/design/human-interface-guidelines/outline-views#Best-practices)

アウトラインビューはテキストベースのコンテンツの表示に適しており、通常は[分割ビュー](https://developer.apple.com/jp/design/human-interface-guidelines/split-views)の先頭側に配置され、反対側にその関連コンテンツが表示されます。

**階層型でないデータを表示する場合はアウトラインビューではなくテーブルを使用する。** ガイダンスは、[リストおよびテーブル](/jp/design/human-interface-guidelines/lists-and-tables)を参照してください。

**データ階層は最初の列にのみ表示する。** ほかの列には、プライマリ列に表示された階層型データの属性を表示できます。

**コンテキストが分かるような列見出しを使用する。** 名詞や短い名詞句による[タイトルに適したスタイル](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64)を使用し、句読点は付けません。特に、末尾にコロンは付けないようにしてください。複数列のアウトラインビューには必ず列見出しを付けます。1列のアウトラインビューに列見出しを付けない場合は、ラベルなど方法で十分なコンテキストを提供してください。

**ユーザが列見出しをクリックしてアウトラインビューを並べ替えられるようにする。** 並べ替え可能なアウトラインビューでは、ユーザが列見出しをクリックして列の昇順または降順で行を並べ替えることができます。必要な場合は、2つ目以降の列に基づいた内部的な並べ替えを追加で実装できます。ユーザがプライマリ列の見出しをクリックすると、各階層レベルで並べ替えが実行されます。例えばFinderでは、すべてのトップレベルフォルダが並び替えられ、各フォルダ内の項目も並び替えられます。ユーザがすでに並べ替えられている列の見出しをクリックした場合は、フォルダとその内容が逆順に並べ替えられます。

**ユーザが列の幅を変更できるようにする。** 多くの場合、アウトラインビューに表示されるデータの幅はまちまちです。列よりも長いデータを表示できるように、必要に応じて列の幅を調整できるようにすることが重要です。

**入れ子のコンテナをユーザが簡単に展開したり折りたたんだりできるようにする。** 例えば、Finderのウインドウでフォルダの開閉用三角ボタンをクリックすると、そのフォルダのみが展開されます。Optionキーを押しながら開閉用三角ボタンをクリックすると、すべてのサブフォルダが展開されます。

**ユーザが項目を展開した状態を維持する。** アウトラインビューでユーザが特定の項目に到達するためにいくつかのレベルを展開した場合、次回もその項目が表示されるように展開状態を保存します。このようにすれば、同じ場所に到達するためにユーザが同じ操作を繰り返す必要はありません。

**複数列のアウトラインビューでは行の色を交互にする。** 行の色を交互にすると、幅の広いアウトラインビューの場合は特に、上下の行にずれることなく行の内容を左右に追いやすくなります。

**アプリ内で理にかなう場合にユーザがデータを編集できるようにする。** ユーザは通常、編集可能なアウトラインビューでセルを1回クリックすればその内容を編集できる、と考えます。ただし、セルのダブルクリックは、これとは異なる反応となる場合があります。例えば、ファイルを表示するアウトラインビューでは、ファイル名を1回クリックすると名前を変更できるようになり、ダブルクリックするとファイルが開くという動作が一般的です。適切な場合には、行の並べ替え、追加、削除もできるようにしてください。

**セルのテキストを切り捨てるのではなく、中央に省略記号を挿入して切り詰める。** 中央に省略記号を挿入すると、セルのテキストの先頭と末尾が保持されるので、テキストを切り捨てるよりも、内容を区別および認識しやすくなります。

**内容が多いアウトラインビューでは、検索フィールドから値を素早く検索できるようにする。** 主要機能としてアウトラインビューが含まれるウインドウでは、通常、ツールバーに検索フィールドが含まれています。ガイダンスは[検索フィールド](/jp/design/human-interface-guidelines/search-fields)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/outline-views#Platform-considerations)

 _iOS、iPadOS、tvOS、visionOS、watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/outline-views#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/outline-views#Related)

[カラム表示](/jp/design/human-interface-guidelines/column-views)

[リストとテーブル](/jp/design/human-interface-guidelines/lists-and-tables)

[分割ビュー](/jp/design/human-interface-guidelines/split-views)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/outline-views#Developer-documentation)

[`OutlineGroup`](/documentation/SwiftUI/OutlineGroup) — SwiftUI

[`NSOutlineView`](/documentation/AppKit/NSOutlineView) — AppKit

#### [ビデオ](/jp/design/human-interface-guidelines/outline-views#Videos)

[](https://developer.apple.com/videos/play/wwdc2020/10031)
