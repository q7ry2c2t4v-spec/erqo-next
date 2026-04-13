# 編集メニュー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/edit-menus

# 編集メニュー

編集メニューには、コピー、選択、翻訳、調べるなどの関連コマンドが表示されます。編集メニューから、現在のビューで選択状態になっているコンテンツを変更することもできます。

![選択されたテキストから伸びる図案化された編集メニュー。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/377d5dd922a53789133dbba5f6bdff1d/components-edit-menu-intro%402x.png)

編集メニューのコマンドは、テキストだけでなく、選択可能な多くのタイプのコンテンツに適用できます。これらには、画像、ファイルをはじめ、連絡先カード、グラフ、地図上の場所のようなオブジェクトも含まれます。iOS、iPadOS、visionOSでは、選択された項目のデータタイプをシステムが自動的に検知するため、そのデータタイプに関連するアクションが編集メニューに追加されることがあります。例えば、住所が選択されると、 _経路を検索_ のような項目が編集メニューに追加される場合があります。

編集メニューの見た目と動作は、プラットフォームごとにわずかに異なります。

  * iOSでは、ユーザがビュー内のコンテンツをタッチして押さえたままにするかダブルタップして選択すると、コマンドが横方向に並んだコンパクトな編集メニューが表示されます。末尾側のシェブロンをタップすると、[コンテキストメニュー](/jp/design/human-interface-guidelines/context-menus)に展開できます。

  * iPadOSでは、ユーザの開き方によって編集メニューの見た目が異なります。ユーザがタッチ操作で開いた編集メニューは、コンパクトな横向きの見た目になります。これに対し、ユーザがキーボードやポインティングデバイスで開いた編集メニューは、コンテキストメニューに直接表示されます。

  * macOSでは、アプリのメニューバーの[編集メニュー](/jp/design/human-interface-guidelines/the-menu-bar#Edit-menu)に加えて、編集作業中にユーザが表示できるコンテキストメニューから編集関連のコマンドにアクセスできます。

  * visionOSのユーザは、標準の[ピンチして押さえたままにする](/jp/design/human-interface-guidelines/gestures#Standard-gestures)ジェスチャを使って編集メニューを水平バーとして開くことも、コンテキストメニュー内で開くこともできます。

tvOSとwatchOSの操作環境ではコンテンツの編集作業はめったに生じないため、これらのプラットフォームで編集メニューは提供されません。

## [ベストプラクティス](/jp/design/human-interface-guidelines/edit-menus#Best-practices)

**できるだけシステムが提供する編集メニューを使う。** ユーザはシステムが提供するコンポーネントのコンテンツと動作に慣れ親しんでいます。同じコマンドを提示するカスタムメニューを作成すると冗長になり、混乱の原因になります。標準の編集メニューのコマンドについて詳しくは、[`UIResponderStandardEditActions`](/documentation/UIKit/UIResponderStandardEditActions)を参照してください。

**システムで定義されたユーザがよく知っている操作で編集メニューを表示できるようにする。** ユーザは例えば、タッチスクリーンをタッチして押さえたままにしたり、visionOSでピンチして押さえたままにしたり、接続されたトラックパッドやキーボードを使って副ボタンをクリックしたりする操作を想定しています。編集メニューを開く操作はプラットフォームによって異なる可能性があるとはいえ、標準的なタスクを実行するためにカスタムの操作を覚えなければならないアプリはユーザに喜ばれません。

**現在の状況と関連性の高いコマンドを提示し、適用できないコマンドはメニューから取り除くか暗くして目立たなくする。** 例えば、何も選択されていないときは、コピーやカットなど選択箇所を必要とするコマンドは表示しないようにします。同様に、ペーストするデータが何もないときは、ペーストコマンドを表示しないようにします。

**システムが提供するコマンドに関連するカスタムコマンドはその近くに表示する。** 例えば、カスタムのフォーマットコマンドを提供する場合、フォーマットセクションでシステムが提供するコマンドのあとにそれらのカスタムコマンドを表示すれば、ユーザに違和感を抱かせない順序を維持できます。大量のカスタムコマンドでユーザに圧迫感を与えないようにしてください。

**必要な場合はユーザが編集不可テキストを選択してコピーできるようにする。** 画像のキャプションやソーシャルメディアの状況などの静的なコンテンツを、メッセージ、メモ、Web検索などにペーストできるとユーザには便利です。原則として、コンテンツのテキストはコピーできる対象に含めますが、コントロールのラベルは除外してください。

**可能な限り取り消し/やり直しに対応する。** ほかのすべてのメニューと同様、編集メニューのアクションを実行する前にユーザの確認は求められないため、直前の状態に戻せる取り消し/やり直しコマンドをユーザが簡単に使えるようにしてください。ガイダンスは、[取り消し/やり直し](/jp/design/human-interface-guidelines/undo-and-redo)を参照してください。

**基本的に、編集メニューの項目と同じ機能を実行するコントロールを別に実装することは避ける。** ユーザは、編集メニューからよく知っている編集コマンドを選んだり、標準のキーボードショートカットを使ったりできると考えます。機能が重複するコントロールを提示すると、インターフェイスの見た目がすっきりせず、ユーザにとって価値ある新たなアクションを提示するためのスペースも減る可能性があります。

**必要に応じて、さまざまなタイプの削除コマンドの違いを明確化する。** 例えば、「削除」のメニュー項目はDeleteキーの押下と同じように動作しますが、「カット」のメニュー項目は選択されたコンテンツをシステムのペーストボードにコピーしてから削除します。

## [コンテンツ](/jp/design/human-interface-guidelines/edit-menus#Content)

**カスタムコマンドに簡潔なラベルを付ける。** そのコマンドが実行するアクションを簡潔に説明する動詞または短い動詞句を使います。ガイダンスは、[ラベル](/jp/design/human-interface-guidelines/labels)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/edit-menus#Platform-considerations)

 _visionOSに追加の考慮事項はありません。tvOSとwatchOSには対応していません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/edit-menus#iOS-iPadOS)

**編集メニューが必ず両方のスタイルで効果的に動作するようにする。** ユーザがMulti-Touchジェスチャを使用して開く場合はコンパクトな横向きスタイルの編集メニューが、キーボードやポインティングデバイスを使用して開く場合は縦向きスタイルの編集メニューが表示されます。縦向きのメニューレイアウトの使い方についてのガイダンスは、[「メニュー」＞「iOS、iPadOS」](/jp/design/human-interface-guidelines/menus#iOS-iPadOS)を参照してください。

**必要に応じて編集メニューの表示位置を調整する。** 利用できるスペースにもよりますが、デフォルトのメニュー位置は挿入ポイントや選択された領域の上か下です。操作対象のコンテンツを示す視覚的なインジケータも表示されます。メニューの形状やポインタ自体は変更できませんが、メニューの位置は変更できます。例えば、重要なコンテンツやインターフェイスコンポーネントと重ならないように、メニューを移動する必要が生じる場合があります。

### [macOS](/jp/design/human-interface-guidelines/edit-menus#macOS)

macOSアプリの編集メニューの項目の順序について詳しくは、[編集メニュー](/jp/design/human-interface-guidelines/the-menu-bar#Edit-menu)を参照してください。

## [リソース](/jp/design/human-interface-guidelines/edit-menus#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/edit-menus#Related)

[メニュー](/jp/design/human-interface-guidelines/menus)

[コンテキストメニュー](/jp/design/human-interface-guidelines/context-menus)

[メニューバー](/jp/design/human-interface-guidelines/the-menu-bar)

[取り消し/やり直し](/jp/design/human-interface-guidelines/undo-and-redo)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/edit-menus#Developer-documentation)

[`UIEditMenuInteraction`](/documentation/UIKit/UIEditMenuInteraction) — UIKit

[`NSMenu`](/documentation/AppKit/NSMenu) — AppKit

## [変更履歴](/jp/design/human-interface-guidelines/edit-menus#Change-log)

日付| 変更内容  
---|---  
2023年6月21日| visionOSのガイダンスを追加するために更新。  
2022年9月14日| iPadOSで両方の編集メニュースタイルに対応することに関するガイドを追加。
