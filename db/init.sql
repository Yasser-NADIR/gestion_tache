
create database test;
use test;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `test`
--

-- --------------------------------------------------------

--
-- Structure de la table `company_settings`
--

CREATE TABLE `company_settings` (
  `setting_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `phone` varchar(25) NOT NULL,
  `address` varchar(255) NOT NULL,
  `logo` varchar(255) NOT NULL,
  `logo_white` varchar(255) NOT NULL,
  `logo_icon` varchar(255) NOT NULL,
  `mainpage_card_text` varchar(500) NOT NULL,
  `footer_text` varchar(255) NOT NULL,
  `facebook_link` varchar(255) NOT NULL,
  `youtube_link` varchar(255) NOT NULL,
  `instagram_link` varchar(255) NOT NULL,
  `print_footer` mediumtext NOT NULL,
  `company_settings_date_updated` date NOT NULL DEFAULT '2024-01-16'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `company_settings`
--

INSERT INTO `company_settings` (`setting_id`, `name`, `phone`, `address`, `logo`, `logo_white`, `logo_icon`, `mainpage_card_text`, `footer_text`, `facebook_link`, `youtube_link`, `instagram_link`, `print_footer`, `company_settings_date_updated`) VALUES
(1, 'organium', '+2127 00746516', 'Votre Adresse Ici', 'logo.png', 'logo_white.png', 'OGRP-64.png', 'TITRE', 'Footer text', 'https://facebook.com/', 'http://youtube.com/', 'https://www.instagram.com/', '', '2024-01-16'),
(2, 'L_name ', 'S_phone ', 'R_address ', '[_logo ', ']_logo_white ', 'B_logo_icon ', 'V_mainpage_card_text ', 'H_footer_text ', 'P_facebook_link ', 'L_youtube_link ', 'C_instagram_link ', 'V_print_footer ', '2024-01-16'),
(3, 'W_name ', 'F_phone ', 'U_address ', 'X_logo ', 'C_logo_white ', ']_logo_icon ', 'T_mainpage_card_text ', '[_footer_text ', 'M_facebook_link ', 'M_youtube_link ', '\\_instagram_link ', 'D_print_footer ', '2024-01-16'),
(4, 'K_name ', 'Z_phone ', 'I_address ', 'Z_logo ', 'K_logo_white ', 'T_logo_icon ', 'F_mainpage_card_text ', 'T_footer_text ', 'Z_facebook_link ', 'W_youtube_link ', 'E_instagram_link ', 'U_print_footer ', '2024-01-16'),
(5, 'E_name ', 'X_phone ', 'B_address ', 'E_logo ', 'C_logo_white ', 'I_logo_icon ', 'R_mainpage_card_text ', 'Z_footer_text ', 'B_facebook_link ', 'C_youtube_link ', 'H_instagram_link ', 'U_print_footer ', '2024-01-16'),
(6, 'R_name ', 'F_phone ', 'G_address ', 'Y_logo ', '\\_logo_white ', 'J_logo_icon ', 'O_mainpage_card_text ', 'I_footer_text ', 'Z_facebook_link ', 'W_youtube_link ', 'X_instagram_link ', 'W_print_footer ', '2024-01-16'),
(7, 'V_name ', 'N_phone ', 'R_address ', 'V_logo ', 'B_logo_white ', 'Q_logo_icon ', 'P_mainpage_card_text ', 'Y_footer_text ', 'T_facebook_link ', 'U_youtube_link ', 'Q_instagram_link ', 'B_print_footer ', '2024-01-16'),
(8, 'R_name ', 'F_phone ', 'E_address ', 'W_logo ', 'Q_logo_white ', '\\_logo_icon ', 'W_mainpage_card_text ', 'R_footer_text ', 'Z_facebook_link ', 'C_youtube_link ', 'V_instagram_link ', 'V_print_footer ', '2024-01-16'),
(9, 'O_name ', 'O_phone ', 'B_address ', 'F_logo ', 'M_logo_white ', 'Q_logo_icon ', '\\_mainpage_card_text ', 'Q_footer_text ', 'B_facebook_link ', 'K_youtube_link ', 'R_instagram_link ', 'K_print_footer ', '2024-01-16'),
(10, 'J_name ', 'G_phone ', 'P_address ', 'O_logo ', '[_logo_white ', 'R_logo_icon ', 'X_mainpage_card_text ', '[_footer_text ', 'Y_facebook_link ', 'D_youtube_link ', 'M_instagram_link ', 'M_print_footer ', '2024-01-16');

-- --------------------------------------------------------

--
-- Structure de la table `f_user`
--

CREATE TABLE `f_user` (
  `id_f_user` int(11) NOT NULL,
  `libelle_famille` varchar(100) NOT NULL,
  `coefficient` int(3) NOT NULL,
  `remarques` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `f_user`
--

INSERT INTO `f_user` (`id_f_user`, `libelle_famille`, `coefficient`, `remarques`) VALUES
(1, 'senior', 1, 'x'),
(3, 'junior', 3, 'x'),
(4, 'dev-ops', 10, 'x'),
(5, 'front-end', 15, 'x'),
(6, 'back-end', 6, 'x'),
(7, 'analyst', 19, 'x'),
(9, 'bi', 20, 'x'),
(10, 'pilot', 30, 'x'),
(11, 'end-user', 1, 'x');

-- --------------------------------------------------------

--
-- Structure de la table `h_det_tache`
--

CREATE TABLE `h_det_tache` (
  `id_h_det_tache` int(11) NOT NULL,
  `id_h_l_ent_tache` int(11) NOT NULL,
  `id_tache` int(11) NOT NULL,
  `h_debut` time(6) NOT NULL DEFAULT '00:01:00.000000',
  `h_fin` time(6) NOT NULL DEFAULT '23:59:00.000000',
  `temps_diff` int(11) NOT NULL,
  `coefficient` int(3) NOT NULL,
  `prix_calc` int(11) NOT NULL,
  `remarques` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `h_det_tache`
--

INSERT INTO `h_det_tache` (`id_h_det_tache`, `id_h_l_ent_tache`, `id_tache`, `h_debut`, `h_fin`, `temps_diff`, `coefficient`, `prix_calc`, `remarques`) VALUES
(9, 9, 5, '00:01:00.000000', '23:59:00.000000', 23, 15, 21570, 'test2'),
(10, 9, 1, '00:01:00.000000', '23:59:00.000000', 23, 50, 71900, 'test3'),
(11, 10, 1, '00:01:00.000000', '23:59:00.000000', 23, 50, 71900, 'test'),
(12, 10, 1, '00:01:00.000000', '23:59:00.000000', 23, 50, 71900, 'test'),
(13, 10, 1, '00:01:00.000000', '23:59:00.000000', 23, 50, 71900, 'test'),
(14, 10, 4, '00:01:00.000000', '23:59:00.000000', 23, 50, 71900, 'test'),
(15, 10, 1, '00:01:00.000000', '23:59:00.000000', 23, 50, 71900, 'test'),
(16, 9, 5, '15:29:00.000000', '18:29:00.000000', 0, 15, 2700, 'couocu'),
(17, 13, 5, '21:22:00.000000', '22:22:00.000000', 60, 15, 900, 't1'),
(18, 13, 6, '13:34:00.000000', '15:34:00.000000', 120, 7, 840, 't2'),
(19, 13, 7, '13:56:00.000000', '17:56:00.000000', 0, 26, 6240, ''),
(21, 12, 6, '13:34:00.000000', '15:34:00.000000', 120, 7, 840, 't2'),
(22, 12, 1, '00:01:00.000000', '23:59:00.000000', 23, 50, 71900, 'test'),
(23, 12, 5, '15:29:00.000000', '18:29:00.000000', 0, 15, 2700, 'couocu'),
(24, 14, 4, '01:44:00.000000', '05:44:00.000000', 240, 105, 25200, 't1'),
(25, 14, 7, '05:45:00.000000', '06:48:00.000000', 63, 26, 1638, 't2'),
(26, 15, 7, '02:04:00.000000', '06:04:00.000000', 240, 26, 6240, 't1'),
(27, 16, 4, '02:15:00.000000', '05:15:00.000000', 180, 10, 1800, 't1'),
(28, 17, 6, '19:43:00.000000', '21:43:00.000000', 120, 6, 720, 'Toto'),
(29, 11, 5, '15:16:00.000000', '20:16:00.000000', 0, 15, 4500, ''),
(30, 18, 4, '22:31:00.000000', '23:31:00.000000', 60, 10, 600, 't1');

-- --------------------------------------------------------

--
-- Structure de la table `h_ent_tache`
--

CREATE TABLE `h_ent_tache` (
  `id_h_ent_tache` int(11) NOT NULL,
  `libelle_journee` varchar(100) NOT NULL,
  `id_users` int(11) NOT NULL,
  `date_operation` date NOT NULL,
  `remarques` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `h_ent_tache`
--

INSERT INTO `h_ent_tache` (`id_h_ent_tache`, `libelle_journee`, `id_users`, `date_operation`, `remarques`) VALUES
(9, 'project 1', 10, '2024-07-17', 'raf'),
(10, 'project 2', 2, '2024-07-12', 'raf'),
(11, 'project 2', 11, '2024-07-13', 'raf'),
(12, 'project 3', 6, '2024-07-15', 'raf'),
(13, 'project 1', 11, '2024-07-13', 'raf'),
(14, 'project 2', 4, '2024-07-14', 'raf'),
(15, 'project 2', 4, '2024-07-14', 'raf'),
(16, 'project 1', 1, '2024-07-15', 'raf'),
(17, 'project 3', 3, '2024-07-15', 'raf'),
(18, 'projet principlale', 3, '2024-08-08', 'test');

-- --------------------------------------------------------

--
-- Structure de la table `region`
--

CREATE TABLE `region` (
  `id` tinyint(4) NOT NULL,
  `nom_region` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `region`
--

INSERT INTO `region` (`id`, `nom_region`) VALUES
(1, 'Alsace'),
(2, 'Aquitaine'),
(3, 'Auvergne'),
(4, 'Basse-Normandie'),
(5, 'Bourgogne'),
(6, 'Bretagne'),
(7, 'Centre'),
(8, 'Champagne-Ardenne'),
(9, 'Corse'),
(10, 'Dom-Tom'),
(11, 'Franche-Comté'),
(12, 'Haute-Normandie'),
(13, 'Ile de France'),
(14, 'Languedoc-Roussillon'),
(15, 'Limousin'),
(16, 'Lorraine'),
(17, 'Midi-Pyrénées'),
(18, 'Nord-Pas-de-Calais'),
(19, 'Pays de la Loire'),
(20, 'Picardie'),
(21, 'Poitou-Charentes'),
(22, 'PACA'),
(23, 'Rhône-Alpes');

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `req_f_user`
-- (Voir ci-dessous la vue réelle)
--
CREATE TABLE `req_f_user` (
`nbr_libelle_famille` bigint(21)
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `req_g_tache`
-- (Voir ci-dessous la vue réelle)
--
CREATE TABLE `req_g_tache` (
`libelle_tache` varchar(100)
,`somme_tache` decimal(32,0)
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `req_g_tache_user`
-- (Voir ci-dessous la vue réelle)
--
CREATE TABLE `req_g_tache_user` (
`nom` varchar(100)
,`libelle_tache` varchar(100)
,`somme_tache` decimal(32,0)
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `req_h_det_tache`
-- (Voir ci-dessous la vue réelle)
--
CREATE TABLE `req_h_det_tache` (
`id_h_det_tache` int(11)
,`id_h_l_ent_tache` int(11)
,`id_tache` int(11)
,`h_debut` time(6)
,`h_fin` time(6)
,`temps_diff` int(11)
,`coefficient` int(3)
,`prix_calc` int(11)
,`remarques` varchar(100)
,`libelle_tache` varchar(100)
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `req_h_ent_tache`
-- (Voir ci-dessous la vue réelle)
--
CREATE TABLE `req_h_ent_tache` (
`id_h_ent_tache` int(11)
,`libelle_journee` varchar(100)
,`id_users` int(11)
,`date_operation` date
,`remarques` varchar(100)
,`nom` varchar(100)
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `req_h_tache`
-- (Voir ci-dessous la vue réelle)
--
CREATE TABLE `req_h_tache` (
`id_h_ent_tache` int(11)
,`libelle_journee` varchar(100)
,`id_users` int(11)
,`date_operation` date
,`remarques` varchar(100)
,`nom` varchar(100)
,`id_h_det_tache` int(11)
,`id_h_l_ent_tache` int(11)
,`id_tache` int(11)
,`h_debut` time(6)
,`h_fin` time(6)
,`temps_diff` int(11)
,`coefficient` int(3)
,`prix_calc` int(11)
,`remarques1` varchar(100)
,`libelle_tache` varchar(100)
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `req_nbr_users_famille`
-- (Voir ci-dessous la vue réelle)
--
CREATE TABLE `req_nbr_users_famille` (
`libelle_famille` varchar(100)
,`nbr_utilisateur` bigint(21)
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `req_taches`
-- (Voir ci-dessous la vue réelle)
--
CREATE TABLE `req_taches` (
`nombre_de_tache` bigint(21)
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `req_users`
-- (Voir ci-dessous la vue réelle)
--
CREATE TABLE `req_users` (
`nbr_users` bigint(21)
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `req_users_famille`
-- (Voir ci-dessous la vue réelle)
--
CREATE TABLE `req_users_famille` (
`id_users` int(11)
,`nom` varchar(100)
,`age` int(3)
,`email` varchar(100)
,`libelle_famille` varchar(100)
);

-- --------------------------------------------------------

--
-- Structure de la table `tache`
--

CREATE TABLE `tache` (
  `id_tache` int(11) NOT NULL,
  `libelle_tache` varchar(100) NOT NULL,
  `coefficient` int(3) NOT NULL,
  `remarques` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `tache`
--

INSERT INTO `tache` (`id_tache`, `libelle_tache`, `coefficient`, `remarques`) VALUES
(1, 'coding', 1, 'rmq tache 1'),
(4, 'testing', 10, 'rmq tache 100'),
(5, 'designing', 15, 'rmq tache 15'),
(6, 'explaining', 6, 'rmq tache 6'),
(7, 'deploying', 26, 'rmq tache  26'),
(8, 'analyzing', 30, 'rmq famille 30');

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` text NOT NULL,
  `email` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password`) VALUES
(1, 'un', 'un', 'un');

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id_users` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `age` int(3) NOT NULL,
  `email` varchar(100) NOT NULL,
  `id_f_user` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id_users`, `nom`, `age`, `email`, `id_f_user`) VALUES
(1, 'john', 25, 'john@gmail.com', 1),
(2, 'tom', 20, 'tom@gmail.com', 1),
(3, 'benjamin', 250, 'benjamin@gmail.com', 1),
(4, 'ted', 300, 'ted@gmail.com', 1),
(5, 'ryan', 20, 'ryan@gmail.com', 1),
(6, 'ahmed', 1500, 'ahmed@gmail.com', 5),
(7, 'joseph', 200, 'joseph@gmail.com', 5),
(8, 'ryad', 2000, 'ryad@gmail.com', 5),
(9, 'bill', 60, 'bill@gmail.com', 6),
(10, 'bob', 17, 'bob@gmail.com', 6),
(11, 'ramu', 13, 'ramu@gmail.com', 3),
(12, 'ellisa', 25, 'ellisa@gmail.com', 1),
(13, 'miryam', 99, 'miryam@gmail.com', 5);


---------------------------------------------------------------
---------------------------------------------------------------
---------------------------------------------------------------







--
-- Index pour les tables déchargées
--

--
-- Index pour la table `company_settings`
--
ALTER TABLE `company_settings`
  ADD PRIMARY KEY (`setting_id`);

--
-- Index pour la table `f_user`
--
ALTER TABLE `f_user`
  ADD PRIMARY KEY (`id_f_user`);

--
-- Index pour la table `h_det_tache`
--
ALTER TABLE `h_det_tache`
  ADD PRIMARY KEY (`id_h_det_tache`);

--
-- Index pour la table `h_ent_tache`
--
ALTER TABLE `h_ent_tache`
  ADD PRIMARY KEY (`id_h_ent_tache`);

--
-- Index pour la table `region`
--
ALTER TABLE `region`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `tache`
--
ALTER TABLE `tache`
  ADD PRIMARY KEY (`id_tache`);

--
-- Index pour la table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_users`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `company_settings`
--
ALTER TABLE `company_settings`
  MODIFY `setting_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT pour la table `f_user`
--
ALTER TABLE `f_user`
  MODIFY `id_f_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT pour la table `h_det_tache`
--
ALTER TABLE `h_det_tache`
  MODIFY `id_h_det_tache` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT pour la table `h_ent_tache`
--
ALTER TABLE `h_ent_tache`
  MODIFY `id_h_ent_tache` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT pour la table `region`
--
ALTER TABLE `region`
  MODIFY `id` tinyint(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT pour la table `tache`
--
ALTER TABLE `tache`
  MODIFY `id_tache` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT pour la table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id_users` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;
