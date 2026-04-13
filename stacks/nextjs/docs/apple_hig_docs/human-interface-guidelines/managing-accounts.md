# アカウントの管理

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/managing-accounts

# アカウントの管理

必要以上に操作感を損なう障壁にならなければ、アカウントはユーザがコンテンツを利用し、詳細な個人情報を記録するための便利な方法になり得ます。

![人のスケッチ。個人情報を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせるオレンジ色になっています。](https://docs-assets.developer.apple.com/published/a3a6931b823bb3f190ce1a3d9dcc1be4/patterns-managing-accounts-intro%402x.png)

アカウントの作成は、アプリやゲームの主要機能に必要な場合にのみユーザに要求します。それ以外の場合は、アカウントなしでアプリやゲームを楽しめるようにしてください。アカウントが必要な場合は、ユーザがいくつものアカウントや認証手法を覚えなくてもすむように、[Appleでサインイン](/jp/design/human-interface-guidelines/sign-in-with-apple)を使った信頼できる一貫したサインイン手段を提供することをおすすめします。

## [ベストプラクティス](/jp/design/human-interface-guidelines/managing-accounts#Best-practices)

**アカウントを作成するメリットおよびサインアップ方法について説明する。** アプリやゲームにアカウントが必要な場合は、アカウントが必要な理由とメリットについて簡潔かつ分かりやすく説明する文言を作成し、それをサインインビューに表示します。

**サインインを要求するタイミングはできるだけ遅らせる。** 多くのユーザは、アプリを使う意義を何も見いだせていないうちにサインインを要求されると、そこでやめてしまいます。こうした状況を避けるため、ユーザにそのような要求をする前に、アプリやゲームで何ができるかという感触をユーザがつかめる機会を設けてください。例えば、ショッピングアプリでは、ユーザが自由に商品をブラウズできるようにして、いよいよ購入するというタイミングで初めてサインインを要求するのがよいでしょう。

**iOS、iPadOS、macOS、visionOSのアプリで「Appleでサインイン」を使用していない場合は、パスキーの使用を優先する。** パスキーを使えば、ユーザがパスワードを作成して入力する必要がないので、アカウントの作成と認証が簡素化されます。アプリでパスキーに対応すると、アカウントを新規作成したり既存のアカウントにサインインしたりするときに、ユーザ名を入力するだけですみます。デベロッパ向けのガイダンスは、[パスキーに対応する](/documentation/AuthenticationServices/supporting-passkeys)を参照してください。認証にパスワードの使用を続ける必要がある場合でも、2ファクタ認証によってセキュリティを強化してください（デベロッパ向けのガイダンスは、[iCloudキーチェーン認証コードでログインのセキュリティを確保する](/documentation/AuthenticationServices/securing-logins-with-icloud-keychain-verification-codes)を参照してください）。

**ユーザに提供する認証方法を明確に示す。** 例えば、Face IDでアプリにサインインするためのボタンには、「サインイン」のような汎用的なタイトルではなく、「Face IDでサインイン」のようなタイトルを付けます。

**アプリの使用環境で利用可能な認証方法のみを提示する。** 例えば、Face IDを搭載していないデバイスではFace ID方式は提示しません。デバイスの機能をチェックして、適切な用語を使用してください。デベロッパ向けのガイダンスは、[`LABiometryType`](/documentation/LocalAuthentication/LABiometryType)を参照してください。

**基本的にアプリ固有の設定で生体認証を有効化することは避ける。** 生体認証はユーザがシステムレベルでオンにします。アプリ内設定があると、これと重複してユーザが混乱する可能性があります。

**アカウントの認証で _パスコード_ という用語を使わないようにする。**デバイスをロック解除したり、Appleのサービスの認証を行ったりするためにユーザが作成するのがパスコードです。この用語をアプリやゲームのインターフェイスで使うと、パスコードをアプリやゲームで再利用するのかとユーザが誤解するおそれがあります。

## [アカウントの削除](/jp/design/human-interface-guidelines/managing-accounts#Deleting-accounts)

アプリやゲームの中でユーザがアカウントを簡単に作成できるようにする一方で、アカウントの無効化だけでなく、削除も簡単にできるようにする必要があります。以下のガイドラインに従うことに加え、アカウントの削除および忘れられる権利に関するそれぞれの地域の法規制を必ず理解し、順守してください。

重要

法規制によって、アカウントやデジタルヘルスケアレコードなどの情報を維持すること、または特定のアカウント削除プロセスに従うことがアプリに義務付けられている場合は、アプリが維持しなければならない情報やアカウント、およびアプリが従わなければならないプロセスをユーザが理解できるよう、状況を明確に説明してください。

**アプリやゲーム内でアカウントを削除する分かりやすい方法を用意する。** ユーザがアプリ内でアカウント削除を実行できない場合は、アカウントを削除できるWebページに直接アクセスできるリンクを提供する必要があります。リンクは見つけやすくしてください。例えば、プライバシーポリシーや利用規約のページに埋め込んだりしてはなりません。

デベロッパ向けメモ

ユーザが[Appleでサインイン](/jp/design/human-interface-guidelines/sign-in-with-apple)を利用してアプリ内でアカウントを作成した場合は、アカウントの削除の際に、関連するトークンを無効化してください。[`Token revocation`](/documentation/SigninwithAppleRESTAPI/Revoke-tokens)を参照してください。

**アカウントの削除をアプリやゲーム内から行うかWebサイトから行うかにかかわらず手順の一貫性を保つ。** 例えば、一方の削除の手順を他方より長くしたり複雑にしたりしないでください。

**ユーザがアカウントの削除をスケジュールできるようにする。** このようにすれば、サービス期間を最大限利用できたり、サブスクリプションの自動更新が来るまでアカウントを保持したりできるため、ユーザの利便性が高まります。アカウントの削除をスケジュールする方法を提供する場合は、直ちに削除するオプションも提供してください。

**アカウントの削除がいつ完了するかをユーザに知らせ、実際に完了したら通知する。** アカウントを完全に削除するまでに時間がかかる場合もあるので、削除プロセスの現在の状況と、次に発生する予定のプロセスを常にユーザに知らせておくのは大切です。

**アプリ内購入に対応する場合は、アカウントを削除した場合の請求やキャンセルの手順についてユーザに説明する。** 例えば、以下のようなシナリオについて理解できるようにしておく必要があるでしょう:

  * 自動更新可能なサブスクリプションの請求は、ユーザがアカウントを削除したかどうかを問わず、ユーザがサブスクリプションをキャンセルするまで引き続きAppleを通じて行われます。

  * 先にアカウントを削除した場合は、サブスクリプションをキャンセルするか払い戻しを要求する必要があります。

ユーザがこれらのシナリオを理解できるよう支援するだけでなく、サブスクリプションをキャンセルしたり、購入を管理したりする方法についての情報を提供してください。ガイダンスは、[サブスクリプション管理機能を実装する](/jp/design/human-interface-guidelines/in-app-purchase#Helping-people-manage-their-subscriptions)および[アプリ内課金に関するサポートを提供する](/jp/design/human-interface-guidelines/in-app-purchase#Providing-help-with-in-app-purchases)を参照してください。

注意

ユーザがアプリを使用してサブスクリプションを購入しなかったとしても、アカウントの削除に対応しておく必要に変わりはありません。

## [TVプロバイダのアカウント](/jp/design/human-interface-guidelines/managing-accounts#TV-provider-accounts)

人気のある多くのTVプロバイダは、アプリごとに認証する必要をなくすため、システムレベルでユーザにアカウントへのサインインを求めています。開発するTVプロバイダアプリでユーザにサインインを要求する場合、TVプロバイダ認証を使用して最も効率のよいオンボーディング体験を提供してください。

**ユーザがシステムレベルでサインインしている場合はサインアウトオプションを表示しない。** アプリにサインアウトオプションを含める必要がある場合は、「設定」＞「TVプロバイダ」と選択してアカウントからサインアウトするようにというプロンプトを表示する必要があります。

**プライバシーコントロールを調整してサインアウトするようにという指示はしないこと。** 「設定」＞「プライバシー」にあるTVプロバイダのコントロールはサインアウトのメカニズムではありません。これらは、TVプロバイダのアカウントを利用できるアプリをユーザが効果的に管理するための設定です。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/managing-accounts#Platform-considerations)

 _iOS、iPadOS、macOS、visionOSに追加の考慮事項はありません。_

### [tvOS](/jp/design/human-interface-guidelines/managing-accounts#tvOS)

ほとんどのユーザはキーボードではなくリモコンでApple TVを操作します。情報の入力は必要最小限にとどめてください。

**できるだけユーザが別のデバイスでサインアップまたは認証するようにする。** Appに関連したドメインを設定すると、Apple TVはほかのデバイスと連係して、[Appleでサインイン](/jp/design/human-interface-guidelines/sign-in-with-apple)などのサインイン資格情報を安全に提案できます。デベロッパ向けのガイダンスは、[関連したドメインの設定](/documentation/Xcode/configuring-an-associated-domain)を参照してください。

**ユーザが共有アカウントでサインインしている場合は、ユーザが切り替わるたびにプロフィールの選択を要求することは避ける。** tvOS 16以降では、アプリで各個人のプロフィールとユーザデータを別個に保存すると同時に、すべてのユーザと資格情報を共有することができます。このタイプの共有に対応したアプリでは、自動的に現在のユーザのプロフィールを使用できます。共有アカウントへの個別のサインインを求める必要はありません。デベロッパ向けのガイダンスは、[`kSecUseUserIndependentKeychain`](/documentation/Security/kSecUseUserIndependentKeychain)および[`User Management Entitlement`](/documentation/BundleResources/Entitlements/com.apple.developer.user-management)を参照してください。

**データ入力は必要最小限にする。** ある程度の分量の情報を収集する必要がある場合は、別のデバイスでWebサイトに接続するようにユーザに依頼してください。メールアドレスが必要な場合は、最近入力したメールアドレスのリストを含むキーボード画面を表示します。

### [watchOS](/jp/design/human-interface-guidelines/managing-accounts#watchOS)

iCloud同期を使ってキーチェーンを利用できるようにすれば、ユーザ名とパスワードを自動入力してアプリの設定を保持できます。

## [リソース](/jp/design/human-interface-guidelines/managing-accounts#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/managing-accounts#Related)

[オンボーディング](/jp/design/human-interface-guidelines/onboarding)

[Appleでサインイン](/jp/design/human-interface-guidelines/sign-in-with-apple)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/managing-accounts#Developer-documentation)

[パスキーに対応する](/documentation/AuthenticationServices/supporting-passkeys) — Authentication Services

#### [ビデオ](/jp/design/human-interface-guidelines/managing-accounts#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/279)

[](https://developer.apple.com/videos/play/wwdc2024/10143)
