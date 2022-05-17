-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 16, 2022 at 07:34 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hrms`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_designations`
--

CREATE TABLE `admin_designations` (
  `id` bigint(20) NOT NULL,
  `designation` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin_designations`
--

INSERT INTO `admin_designations` (`id`, `designation`) VALUES
(1, 'Junior Developer'),
(2, 'Accountant'),
(3, 'UI designer'),
(4, 'UX designer'),
(5, 'Operations Executive');

-- --------------------------------------------------------

--
-- Table structure for table `admin_holidays`
--

CREATE TABLE `admin_holidays` (
  `id` bigint(20) NOT NULL,
  `date` date NOT NULL,
  `reason` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin_holidays`
--

INSERT INTO `admin_holidays` (`id`, `date`, `reason`) VALUES
(5, '2022-04-14', 'Strike');

-- --------------------------------------------------------

--
-- Table structure for table `admin_payroll`
--

CREATE TABLE `admin_payroll` (
  `id` bigint(20) NOT NULL,
  `basic` double NOT NULL,
  `hra` double NOT NULL,
  `ta` double NOT NULL,
  `pf` double NOT NULL,
  `other_benefits` double NOT NULL,
  `other_deductions` double NOT NULL,
  `net_salary` double NOT NULL,
  `date` date NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `status` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin_payroll`
--

INSERT INTO `admin_payroll` (`id`, `basic`, `hra`, `ta`, `pf`, `other_benefits`, `other_deductions`, `net_salary`, `date`, `user_id`, `status`) VALUES
(1, 20000, 8000, 4000, 2400, 0, 0, 29600, '2022-03-08', 2, 'approved'),
(2, 40000, 16000, 8000, 4800, 300, 100, 59400, '2022-03-08', 3, 'approved'),
(3, 30000, 12000, 6000, 3600, 0, 0, 44400, '2022-03-08', 5, 'approved'),
(4, 27000, 10800, 0, 3240, 0, 0, 34560, '2022-03-08', 9, 'approved'),
(5, 25000, 10000, 5000, 0, 0, 0, 40000, '2022-03-08', 12, 'approved'),
(6, 50000, 20000, 10000, 0, 0, 0, 80000, '2022-03-08', 15, 'approved'),
(7, 20000, 8000, 4000, 2400, 10, 333.3333333333333, 29276.666666666668, '2022-04-06', 2, 'approved'),
(8, 40000, 16000, 8000, 4800, 0, 0, 59200, '2022-04-06', 3, 'approved'),
(9, 30000, 12000, 6000, 3600, 0, 500, 43900, '2022-04-06', 5, 'approved'),
(10, 27000, 10800, 0, 3240, 0, 0, 34560, '2022-04-06', 9, 'approved'),
(11, 25000, 10000, 5000, 0, 0, 0, 40000, '2022-04-06', 12, 'approved'),
(12, 50000, 20000, 10000, 0, 0, 9166.666666666668, 70833.33333333333, '2022-04-06', 15, 'approved');

-- --------------------------------------------------------

--
-- Table structure for table `admin_salary`
--

CREATE TABLE `admin_salary` (
  `id` bigint(20) NOT NULL,
  `basic_pay` double NOT NULL,
  `hra` tinyint(1) NOT NULL,
  `ta` tinyint(1) NOT NULL,
  `pf` tinyint(1) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin_salary`
--

INSERT INTO `admin_salary` (`id`, `basic_pay`, `hra`, `ta`, `pf`, `user_id`) VALUES
(1, 20000, 1, 1, 1, 2),
(2, 40000, 1, 1, 1, 3),
(3, 30000, 1, 1, 1, 5),
(4, 27000, 1, 0, 1, 9),
(7, 25000, 1, 1, 0, 12),
(8, 50000, 1, 1, 0, 15);

-- --------------------------------------------------------

--
-- Table structure for table `applicants_applications`
--

CREATE TABLE `applicants_applications` (
  `id` bigint(20) NOT NULL,
  `applied_date` date NOT NULL,
  `selected` varchar(12) NOT NULL,
  `job_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `applicants_applications`
--

INSERT INTO `applicants_applications` (`id`, `applied_date`, `selected`, `job_id`, `user_id`) VALUES
(1, '2022-03-26', 'accepted', 4, 4),
(2, '2022-03-26', 'accepted', 1, 6),
(3, '2022-03-29', 'accepted', 1, 7);

-- --------------------------------------------------------

--
-- Table structure for table `applicants_interviews`
--

CREATE TABLE `applicants_interviews` (
  `id` bigint(20) NOT NULL,
  `interview_date` date NOT NULL,
  `start_time` time(6) NOT NULL,
  `end_time` time(6) NOT NULL,
  `department_id` bigint(20) NOT NULL,
  `job_id` bigint(20) NOT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `applicants_interviews`
--

INSERT INTO `applicants_interviews` (`id`, `interview_date`, `start_time`, `end_time`, `department_id`, `job_id`, `description`) VALUES
(12, '2022-04-27', '10:30:00.000000', '15:30:00.000000', 1, 4, 'This is  interview details for project manager'),
(13, '2022-05-12', '10:30:00.000000', '16:30:00.000000', 1, 1, 'Interview description');

-- --------------------------------------------------------

--
-- Table structure for table `applicants_messages`
--

CREATE TABLE `applicants_messages` (
  `id` bigint(20) NOT NULL,
  `title` varchar(100) NOT NULL,
  `body` longtext NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `applicants_messages`
--

INSERT INTO `applicants_messages` (`id`, `title`, `body`, `date`) VALUES
(1, 'First Message', 'This is the First message by HR Admin', '2022-04-03 04:30:48.031013'),
(2, 'Second Message', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', '2022-04-03 06:09:54.514755'),
(4, 'Another message', 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English.\r\nBy HR', '2022-04-03 06:57:38.066029'),
(5, 'Test Message', 'There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don\'t look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn\'t anything embarrassing hidden in the middle of text.', '2022-04-03 12:32:54.093113'),
(6, 'message', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', '2022-04-03 14:16:26.242140'),
(7, 'Next Message', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Mauris commodo quis imperdiet massa tincidunt nunc pulvinar sapien et. Vitae tortor condimentum lacinia quis. Leo duis ut diam quam nulla porttitor massa id. Sed adipiscing diam donec adipiscing tristique risus nec feugiat in. Sit amet volutpat consequat mauris nunc congue nisi vitae. Vitae tortor condimentum lacinia quis. Amet consectetur adipiscing elit pellentesque habitant morbi tristique senectus et. Mattis vulputate enim nulla aliquet porttitor lacus luctus. Lorem donec massa sapien faucibus et molestie ac. Venenatis a condimentum vitae sapien pellentesque habitant. Mollis nunc sed id semper risus in hendrerit gravida rutrum. Nibh nisl condimentum id venenatis a condimentum vitae. Ullamcorper sit amet risus nullam eget felis. Imperdiet massa tincidunt nunc pulvinar sapien et ligula ullamcorper malesuada.', '2022-04-03 14:16:26.242140'),
(8, 'Company Anniversary', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', '2022-04-07 16:14:43.742635');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can view permission', 1, 'view_permission'),
(5, 'Can add group', 2, 'add_group'),
(6, 'Can change group', 2, 'change_group'),
(7, 'Can delete group', 2, 'delete_group'),
(8, 'Can view group', 2, 'view_group'),
(9, 'Can add content type', 3, 'add_contenttype'),
(10, 'Can change content type', 3, 'change_contenttype'),
(11, 'Can delete content type', 3, 'delete_contenttype'),
(12, 'Can view content type', 3, 'view_contenttype'),
(13, 'Can add session', 4, 'add_session'),
(14, 'Can change session', 4, 'change_session'),
(15, 'Can delete session', 4, 'delete_session'),
(16, 'Can view session', 4, 'view_session'),
(17, 'Can add jobs', 5, 'add_jobs'),
(18, 'Can change jobs', 5, 'change_jobs'),
(19, 'Can delete jobs', 5, 'delete_jobs'),
(20, 'Can view jobs', 5, 'view_jobs'),
(21, 'Can add department', 6, 'add_department'),
(22, 'Can change department', 6, 'change_department'),
(23, 'Can delete department', 6, 'delete_department'),
(24, 'Can view department', 6, 'view_department'),
(25, 'Can add user', 7, 'add_newuser'),
(26, 'Can change user', 7, 'change_newuser'),
(27, 'Can delete user', 7, 'delete_newuser'),
(28, 'Can view user', 7, 'view_newuser'),
(29, 'Can add applicant profile', 8, 'add_applicantprofile'),
(30, 'Can change applicant profile', 8, 'change_applicantprofile'),
(31, 'Can delete applicant profile', 8, 'delete_applicantprofile'),
(32, 'Can view applicant profile', 8, 'view_applicantprofile'),
(33, 'Can add applications', 9, 'add_applications'),
(34, 'Can change applications', 9, 'change_applications'),
(35, 'Can delete applications', 9, 'delete_applications'),
(36, 'Can view applications', 9, 'view_applications'),
(37, 'Can add interviews', 10, 'add_interviews'),
(38, 'Can change interviews', 10, 'change_interviews'),
(39, 'Can delete interviews', 10, 'delete_interviews'),
(40, 'Can view interviews', 10, 'view_interviews'),
(41, 'Can add employee profile', 11, 'add_employeeprofile'),
(42, 'Can change employee profile', 11, 'change_employeeprofile'),
(43, 'Can delete employee profile', 11, 'delete_employeeprofile'),
(44, 'Can view employee profile', 11, 'view_employeeprofile'),
(45, 'Can add attendance', 12, 'add_attendance'),
(46, 'Can change attendance', 12, 'change_attendance'),
(47, 'Can delete attendance', 12, 'delete_attendance'),
(48, 'Can view attendance', 12, 'view_attendance'),
(49, 'Can add leave', 13, 'add_leave'),
(50, 'Can change leave', 13, 'change_leave'),
(51, 'Can delete leave', 13, 'delete_leave'),
(52, 'Can view leave', 13, 'view_leave'),
(53, 'Can add employee designation', 14, 'add_employeedesignation'),
(54, 'Can change employee designation', 14, 'change_employeedesignation'),
(55, 'Can delete employee designation', 14, 'delete_employeedesignation'),
(56, 'Can view employee designation', 14, 'view_employeedesignation'),
(57, 'Can add attendance regulization', 15, 'add_attendanceregulization'),
(58, 'Can change attendance regulization', 15, 'change_attendanceregulization'),
(59, 'Can delete attendance regulization', 15, 'delete_attendanceregulization'),
(60, 'Can view attendance regulization', 15, 'view_attendanceregulization'),
(61, 'Can add salary', 16, 'add_salary'),
(62, 'Can change salary', 16, 'change_salary'),
(63, 'Can delete salary', 16, 'delete_salary'),
(64, 'Can view salary', 16, 'view_salary'),
(65, 'Can add designations', 17, 'add_designations'),
(66, 'Can change designations', 17, 'change_designations'),
(67, 'Can delete designations', 17, 'delete_designations'),
(68, 'Can view designations', 17, 'view_designations'),
(69, 'Can add attendance regularization', 15, 'add_attendanceregularization'),
(70, 'Can change attendance regularization', 15, 'change_attendanceregularization'),
(71, 'Can delete attendance regularization', 15, 'delete_attendanceregularization'),
(72, 'Can view attendance regularization', 15, 'view_attendanceregularization'),
(73, 'Can add crontab', 18, 'add_crontabschedule'),
(74, 'Can change crontab', 18, 'change_crontabschedule'),
(75, 'Can delete crontab', 18, 'delete_crontabschedule'),
(76, 'Can view crontab', 18, 'view_crontabschedule'),
(77, 'Can add interval', 19, 'add_intervalschedule'),
(78, 'Can change interval', 19, 'change_intervalschedule'),
(79, 'Can delete interval', 19, 'delete_intervalschedule'),
(80, 'Can view interval', 19, 'view_intervalschedule'),
(81, 'Can add periodic task', 20, 'add_periodictask'),
(82, 'Can change periodic task', 20, 'change_periodictask'),
(83, 'Can delete periodic task', 20, 'delete_periodictask'),
(84, 'Can view periodic task', 20, 'view_periodictask'),
(85, 'Can add periodic tasks', 21, 'add_periodictasks'),
(86, 'Can change periodic tasks', 21, 'change_periodictasks'),
(87, 'Can delete periodic tasks', 21, 'delete_periodictasks'),
(88, 'Can view periodic tasks', 21, 'view_periodictasks'),
(89, 'Can add solar event', 22, 'add_solarschedule'),
(90, 'Can change solar event', 22, 'change_solarschedule'),
(91, 'Can delete solar event', 22, 'delete_solarschedule'),
(92, 'Can view solar event', 22, 'view_solarschedule'),
(93, 'Can add clocked', 23, 'add_clockedschedule'),
(94, 'Can change clocked', 23, 'change_clockedschedule'),
(95, 'Can delete clocked', 23, 'delete_clockedschedule'),
(96, 'Can view clocked', 23, 'view_clockedschedule'),
(97, 'Can add leave counter', 24, 'add_leavecounter'),
(98, 'Can change leave counter', 24, 'change_leavecounter'),
(99, 'Can delete leave counter', 24, 'delete_leavecounter'),
(100, 'Can view leave counter', 24, 'view_leavecounter'),
(101, 'Can add year counter', 25, 'add_yearcounter'),
(102, 'Can change year counter', 25, 'change_yearcounter'),
(103, 'Can delete year counter', 25, 'delete_yearcounter'),
(104, 'Can view year counter', 25, 'view_yearcounter'),
(105, 'Can add messages', 26, 'add_messages'),
(106, 'Can change messages', 26, 'change_messages'),
(107, 'Can delete messages', 26, 'delete_messages'),
(108, 'Can view messages', 26, 'view_messages'),
(109, 'Can add payroll', 27, 'add_payroll'),
(110, 'Can change payroll', 27, 'change_payroll'),
(111, 'Can delete payroll', 27, 'delete_payroll'),
(112, 'Can view payroll', 27, 'view_payroll'),
(113, 'Can add holidays', 28, 'add_holidays'),
(114, 'Can change holidays', 28, 'change_holidays'),
(115, 'Can delete holidays', 28, 'delete_holidays'),
(116, 'Can view holidays', 28, 'view_holidays');

-- --------------------------------------------------------

--
-- Table structure for table `base_department`
--

CREATE TABLE `base_department` (
  `id` bigint(20) NOT NULL,
  `department_name` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_department`
--

INSERT INTO `base_department` (`id`, `department_name`) VALUES
(1, 'R & D '),
(2, 'General Management'),
(3, 'Finance');

-- --------------------------------------------------------

--
-- Table structure for table `base_jobs`
--

CREATE TABLE `base_jobs` (
  `id` bigint(20) NOT NULL,
  `job_title` varchar(60) NOT NULL,
  `job_description` longtext NOT NULL,
  `location` varchar(60) NOT NULL,
  `posted_on` date NOT NULL,
  `withdraw_date` date NOT NULL,
  `department_id` bigint(20) NOT NULL,
  `skills` longtext NOT NULL,
  `salary` bigint(20) DEFAULT NULL,
  `scheduled` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_jobs`
--

INSERT INTO `base_jobs` (`id`, `job_title`, `job_description`, `location`, `posted_on`, `withdraw_date`, `department_id`, `skills`, `salary`, `scheduled`) VALUES
(1, 'Junior Developer', 'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available', 'Kochi,Kerala', '2022-03-25', '2022-03-25', 1, 'Cloud Computing provides an alternative to the on-premises datacentre. With an on-premises datacentre, we have to manage everything, such as purchasing and installing hardware, virtualization, installing the operating system, and any other required applications, setting up the network, configuring the firewall, and setting up storage for data. After doing all the set-up, we become responsible for maintaining it through its entire lifecycle.', 300000, 1),
(2, 'Senior developer', 'Cloud Computing provides an alternative to the on-premises datacentre. With an on-premises datacentre, we have to manage everything, such as purchasing and installing hardware, virtualization, installing the operating system, and any other required applications, setting up the network, configuring the firewall, and setting up storage for data. After doing all the set-up, we become responsible for maintaining it through its entire lifecycle.', 'Kochi,Kerala', '2022-03-25', '2022-03-26', 1, 'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available', 500000, 0),
(3, 'Accountant', 'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available', 'Kochi,Kerala', '2022-03-25', '2022-09-30', 3, 'Cloud Computing provides an alternative to the on-premises datacentre. With an on-premises datacentre, we have to manage everything, such as purchasing and installing hardware, virtualization, installing the operating system, and any other required applications, setting up the network, configuring the firewall, and setting up storage for data. After doing all the set-up, we become responsible for maintaining it through its entire lifecycle.', 350000, 0),
(4, 'Project Manager', 'Cloud Computing provides an alternative to the on-premises datacentre. With an on-premises datacentre, we have to manage everything, such as purchasing and installing hardware, virtualization, installing the operating system, and any other required applications, setting up the network, configuring the firewall, and setting up storage for data. After doing all the set-up, we become responsible for maintaining it through its entire lifecycle.', 'Kochi,Kerala', '2022-03-25', '2022-03-28', 1, 'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available', 700000, 1),
(5, 'UI developer', 'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available', 'Kochi,Kerala', '2022-03-25', '2022-09-30', 1, 'Lorem ipsum may be used as a placeholder before the final copy is available  Cloud Computing provides an alternative to the on-premises datacentre. With an on-premises datacentre, we have to manage everything, such as purchasing and installing hardware, virtualization, installing the operating system, and any other required applications, setting up the network, configuring the firewall, and setting up storage for data. After doing all the set-up, we become responsible for maintaining it through its entire lifecycle.', 400000, 0),
(6, 'UX developer', 'Cloud Computing provides an alternative to the on-premises datacentre. With an on-premises datacentre, we have to manage everything, such as purchasing and installing hardware, virtualization, installing the operating system, and any other required applications, setting up the network, configuring the firewall, and setting up storage for data. After doing all the set-up, we become responsible for maintaining it through its entire lifecycle.', 'Kochi,Kerala', '2022-03-25', '2022-09-29', 1, 'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available', 350000, 0),
(7, 'Operations Executive', 'Cloud Computing provides an alternative to the on-premises datacentre. With an on-premises datacentre, we have to manage everything, such as purchasing and installing hardware, virtualization, installing the operating system, and any other required applications, setting up the network, configuring the firewall, and setting up storage for data. After doing all the set-up, we become responsible for maintaining it through its entire lifecycle.', 'Kochi,Kerala', '2022-04-04', '2022-09-23', 2, 'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available', 250000, 0),
(8, 'System Administrator', 'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available', 'Kochi,Kerala', '2022-04-04', '2022-09-24', 1, 'Cloud Computing provides an alternative to the on-premises datacentre. With an on-premises datacentre, we have to manage everything, such as purchasing and installing hardware, virtualization, installing the operating system, and any other required applications, setting up the network, configuring the firewall, and setting up storage for data. After doing all the set-up, we become responsible for maintaining it through its entire lifecycle.', 400000, 0),
(9, 'Programmer Trainee', 'Cloud Computing provides an alternative to the on-premises datacentre. With an on-premises datacentre, we have to manage everything, such as purchasing and installing hardware, virtualization, installing the operating system, and any other required applications, setting up the network, configuring the firewall, and setting up storage for data. After doing all the set-up, we become responsible for maintaining it through its entire lifecycle.', 'Kochi,Kerala', '2022-04-04', '2022-09-29', 1, 'Cloud Computing provides an alternative to the on-premises datacentre. With an on-premises datacentre, we have to manage everything, such as purchasing and installing hardware, virtualization, installing the operating system, and any other required applications, setting up the network, configuring the firewall, and setting up storage for data. After doing all the set-up, we become responsible for maintaining it through its entire lifecycle.', 275000, 0);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(17, 'admin', 'designations'),
(28, 'admin', 'holidays'),
(27, 'admin', 'payroll'),
(16, 'admin', 'salary'),
(9, 'applicants', 'applications'),
(10, 'applicants', 'interviews'),
(26, 'applicants', 'messages'),
(2, 'auth', 'group'),
(1, 'auth', 'permission'),
(6, 'base', 'department'),
(5, 'base', 'jobs'),
(3, 'contenttypes', 'contenttype'),
(23, 'django_celery_beat', 'clockedschedule'),
(18, 'django_celery_beat', 'crontabschedule'),
(19, 'django_celery_beat', 'intervalschedule'),
(20, 'django_celery_beat', 'periodictask'),
(21, 'django_celery_beat', 'periodictasks'),
(22, 'django_celery_beat', 'solarschedule'),
(12, 'employees', 'attendance'),
(15, 'employees', 'attendanceregularization'),
(14, 'employees', 'employeedesignation'),
(11, 'employees', 'employeeprofile'),
(13, 'employees', 'leave'),
(24, 'employees', 'leavecounter'),
(25, 'employees', 'yearcounter'),
(4, 'sessions', 'session'),
(8, 'users', 'applicantprofile'),
(7, 'users', 'newuser');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-03-25 13:58:22.441814'),
(2, 'contenttypes', '0002_remove_content_type_name', '2022-03-25 13:58:22.524814'),
(3, 'auth', '0001_initial', '2022-03-25 13:58:22.749436'),
(4, 'auth', '0002_alter_permission_name_max_length', '2022-03-25 13:58:22.802447'),
(5, 'auth', '0003_alter_user_email_max_length', '2022-03-25 13:58:22.813449'),
(6, 'auth', '0004_alter_user_username_opts', '2022-03-25 13:58:22.823452'),
(7, 'auth', '0005_alter_user_last_login_null', '2022-03-25 13:58:22.833455'),
(8, 'auth', '0006_require_contenttypes_0002', '2022-03-25 13:58:22.837207'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2022-03-25 13:58:22.847208'),
(10, 'auth', '0008_alter_user_username_max_length', '2022-03-25 13:58:22.859210'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2022-03-25 13:58:22.870212'),
(12, 'auth', '0010_alter_group_name_max_length', '2022-03-25 13:58:22.896219'),
(13, 'auth', '0011_update_proxy_permissions', '2022-03-25 13:58:22.908221'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2022-03-25 13:58:22.922226'),
(15, 'users', '0001_initial', '2022-03-25 13:58:23.272072'),
(16, 'users', '0002_applicantprofile_last_apply', '2022-03-25 13:58:23.301163'),
(17, 'users', '0003_remove_applicantprofile_first_name_and_more', '2022-03-25 13:58:23.394181'),
(18, 'users', '0004_alter_applicantprofile_cv', '2022-03-25 13:58:23.406125'),
(19, 'users', '0005_alter_applicantprofile_cv', '2022-03-25 13:58:23.423129'),
(20, 'users', '0006_alter_applicantprofile_phone_and_more', '2022-03-25 13:58:23.446134'),
(21, 'admin', '0001_initial', '2022-03-25 13:58:23.531244'),
(22, 'admin', '0002_designations', '2022-03-25 13:58:23.568254'),
(23, 'admin', '0003_alter_salary_ta', '2022-03-25 13:58:23.585257'),
(24, 'admin', '0004_alter_salary_ta', '2022-03-25 13:58:23.600259'),
(25, 'base', '0001_initial', '2022-03-25 13:58:23.721822'),
(26, 'base', '0002_alter_jobs_options', '2022-03-25 13:58:23.729275'),
(27, 'base', '0003_alter_category_options_alter_jobs_options_and_more', '2022-03-25 13:58:23.756282'),
(28, 'base', '0004_alter_jobs_posted_on', '2022-03-25 13:58:23.765290'),
(29, 'base', '0005_jobs_skills', '2022-03-25 13:58:23.798310'),
(30, 'base', '0006_rename_category_department', '2022-03-25 13:58:24.779155'),
(31, 'base', '0007_alter_department_options_and_more', '2022-03-25 13:58:24.996015'),
(32, 'applicants', '0001_initial', '2022-03-25 13:58:25.119310'),
(33, 'applicants', '0002_interviews', '2022-03-25 13:58:25.231651'),
(34, 'applicants', '0003_interviews_description', '2022-03-25 13:58:25.263658'),
(35, 'base', '0008_jobs_salary', '2022-03-25 13:58:25.286646'),
(36, 'base', '0009_alter_jobs_salary', '2022-03-25 13:58:25.333438'),
(37, 'base', '0010_alter_jobs_withdraw_date', '2022-03-25 13:58:25.343440'),
(38, 'users', '0007_alter_applicantprofile_gender', '2022-03-25 13:58:25.371448'),
(39, 'users', '0008_alter_applicantprofile_gender', '2022-03-25 13:58:25.386192'),
(40, 'employees', '0001_initial', '2022-03-25 13:58:25.506033'),
(41, 'employees', '0002_alter_employeeprofile_photo', '2022-03-25 13:58:25.527039'),
(42, 'employees', '0003_alter_employeeprofile_join_date', '2022-03-25 13:58:25.581034'),
(43, 'employees', '0004_remove_employeeprofile_department', '2022-03-25 13:58:25.766076'),
(44, 'employees', '0005_attendance', '2022-03-25 13:58:25.836005'),
(45, 'employees', '0006_alter_attendance_entry_time_and_more', '2022-03-25 13:58:25.920971'),
(46, 'employees', '0007_nightshift', '2022-03-25 13:58:26.005455'),
(47, 'employees', '0008_attendance_shift_delete_nightshift', '2022-03-25 13:58:26.039461'),
(48, 'employees', '0009_alter_attendance_shift', '2022-03-25 13:58:26.112245'),
(49, 'employees', '0010_leave', '2022-03-25 13:58:26.181127'),
(50, 'employees', '0011_remove_leave_leave_date_leave_from_date_and_more', '2022-03-25 13:58:26.314747'),
(51, 'employees', '0012_alter_leave_from_date_alter_leave_from_session_and_more', '2022-03-25 13:58:26.437794'),
(52, 'employees', '0013_leave_approval', '2022-03-25 13:58:26.477758'),
(53, 'employees', '0014_alter_leave_reason', '2022-03-25 13:58:26.531569'),
(54, 'employees', '0015_alter_leave_reason', '2022-03-25 13:58:26.590825'),
(55, 'employees', '0016_employeeprofile_department_and_more', '2022-03-25 13:58:26.698837'),
(56, 'employees', '0017_alter_employeeprofile_department_and_more', '2022-03-25 13:58:27.107589'),
(57, 'employees', '0018_remove_employeeprofile_department', '2022-03-25 13:58:27.261073'),
(58, 'employees', '0019_employeeprofile_department_and_more', '2022-03-25 13:58:27.339868'),
(59, 'employees', '0020_alter_employeeprofile_department_and_more', '2022-03-25 13:58:27.377129'),
(60, 'employees', '0021_alter_employeeprofile_department_and_more', '2022-03-25 13:58:27.739277'),
(61, 'employees', '0022_remove_employeeprofile_department_and_more', '2022-03-25 13:58:28.087079'),
(62, 'employees', '0023_employeedesignation_user', '2022-03-25 13:58:28.153668'),
(63, 'employees', '0024_alter_employeedesignation_user', '2022-03-25 13:58:28.355830'),
(64, 'employees', '0025_remove_employeeprofile_join_date', '2022-03-25 13:58:28.384564'),
(65, 'employees', '0026_alter_employeeprofile_gender', '2022-03-25 13:58:28.414589'),
(66, 'employees', '0027_alter_leave_approval', '2022-03-25 13:58:28.493127'),
(67, 'employees', '0028_alter_leave_leave_type', '2022-03-25 13:58:28.527135'),
(68, 'employees', '0029_leave_applied_date', '2022-03-25 13:58:28.554142'),
(69, 'employees', '0030_alter_leave_applied_date', '2022-03-25 13:58:28.621138'),
(70, 'employees', '0031_alter_leave_from_date_alter_leave_to_date', '2022-03-25 13:58:28.654146'),
(71, 'employees', '0032_attendanceregulization', '2022-03-25 13:58:28.779808'),
(72, 'sessions', '0001_initial', '2022-03-25 13:58:28.815816'),
(73, 'employees', '0033_rename_attendanceregulization_attendanceregularization', '2022-03-25 14:31:14.184328'),
(74, 'applicants', '0004_alter_applications_selected', '2022-03-26 10:21:49.120815'),
(75, 'applicants', '0005_alter_interviews_interview_date', '2022-03-27 04:17:02.366148'),
(76, 'base', '0011_jobs_scheduled', '2022-03-27 05:44:53.231325'),
(77, 'django_celery_beat', '0001_initial', '2022-03-30 04:17:29.082292'),
(78, 'django_celery_beat', '0002_auto_20161118_0346', '2022-03-30 04:17:29.164305'),
(79, 'django_celery_beat', '0003_auto_20161209_0049', '2022-03-30 04:17:29.191315'),
(80, 'django_celery_beat', '0004_auto_20170221_0000', '2022-03-30 04:17:29.201331'),
(81, 'django_celery_beat', '0005_add_solarschedule_events_choices', '2022-03-30 04:17:29.212315'),
(82, 'django_celery_beat', '0006_auto_20180322_0932', '2022-03-30 04:17:29.295247'),
(83, 'django_celery_beat', '0007_auto_20180521_0826', '2022-03-30 04:17:29.350328'),
(84, 'django_celery_beat', '0008_auto_20180914_1922', '2022-03-30 04:17:29.382760'),
(85, 'django_celery_beat', '0006_auto_20180210_1226', '2022-03-30 04:17:29.404674'),
(86, 'django_celery_beat', '0006_periodictask_priority', '2022-03-30 04:17:29.430679'),
(87, 'django_celery_beat', '0009_periodictask_headers', '2022-03-30 04:17:29.466683'),
(88, 'django_celery_beat', '0010_auto_20190429_0326', '2022-03-30 04:17:29.623738'),
(89, 'django_celery_beat', '0011_auto_20190508_0153', '2022-03-30 04:17:29.724130'),
(90, 'django_celery_beat', '0012_periodictask_expire_seconds', '2022-03-30 04:17:29.754135'),
(91, 'django_celery_beat', '0013_auto_20200609_0727', '2022-03-30 04:17:29.767137'),
(92, 'django_celery_beat', '0014_remove_clockedschedule_enabled', '2022-03-30 04:17:29.790143'),
(93, 'django_celery_beat', '0015_edit_solarschedule_events_choices', '2022-03-30 04:17:29.803146'),
(94, 'employees', '0034_leavecounter', '2022-03-30 05:47:07.620321'),
(95, 'employees', '0035_leave_attachments', '2022-03-30 11:25:02.600289'),
(96, 'employees', '0036_alter_leave_attachments', '2022-03-30 12:18:21.201780'),
(97, 'users', '0009_alter_applicantprofile_cv', '2022-03-30 12:18:21.228787'),
(98, 'employees', '0037_yearcounter', '2022-03-31 16:06:00.582641'),
(99, 'employees', '0038_attendance_leave', '2022-04-01 06:25:06.241534'),
(100, 'employees', '0039_alter_attendance_leave', '2022-04-01 08:19:18.267369'),
(101, 'employees', '0040_alter_attendance_leave', '2022-04-01 08:52:34.503951'),
(102, 'employees', '0041_attendance_lno', '2022-04-01 10:31:37.799823'),
(103, 'employees', '0042_auto_20220401_1651', '2022-04-01 11:22:06.132531'),
(104, 'employees', '0043_leave_admin', '2022-04-02 03:30:16.351393'),
(105, 'employees', '0044_alter_leavecounter_date', '2022-04-02 11:54:10.049796'),
(106, 'employees', '0045_attendanceregularization_shift', '2022-04-02 15:56:09.166738'),
(107, 'applicants', '0006_messages', '2022-04-03 03:08:21.562432'),
(108, 'admin', '0005_messages', '2022-04-03 04:00:22.721310'),
(109, 'admin', '0006_delete_messages', '2022-04-03 04:00:22.737294'),
(110, 'applicants', '0007_alter_messages_date', '2022-04-03 04:00:22.745294'),
(111, 'applicants', '0008_alter_messages_date', '2022-04-03 07:03:11.144308'),
(112, 'applicants', '0009_alter_messages_date', '2022-04-03 07:03:11.160234'),
(113, 'admin', '0007_alter_salary_basic_pay', '2022-04-03 13:38:13.251045'),
(114, 'applicants', '0010_alter_messages_date', '2022-04-03 13:38:13.258047'),
(115, 'admin', '0008_alter_salary_basic_pay', '2022-04-03 13:40:29.735127'),
(116, 'applicants', '0011_alter_messages_date', '2022-04-03 13:40:29.742126'),
(117, 'admin', '0009_payroll', '2022-04-03 13:45:50.342344'),
(118, 'applicants', '0012_alter_messages_date', '2022-04-03 13:45:50.350622'),
(119, 'admin', '0010_auto_20220404_1638', '2022-04-04 11:08:12.034563'),
(120, 'applicants', '0013_alter_messages_date', '2022-04-04 11:08:12.038563'),
(121, 'admin', '0011_auto_20220404_1640', '2022-04-04 11:10:17.925650'),
(122, 'applicants', '0014_alter_messages_date', '2022-04-04 11:10:17.928652'),
(123, 'admin', '0012_auto_20220404_1643', '2022-04-04 11:13:36.259468'),
(124, 'applicants', '0015_alter_messages_date', '2022-04-04 11:13:36.263470'),
(125, 'admin', '0013_payroll_status', '2022-04-04 11:35:32.145049'),
(126, 'applicants', '0016_alter_messages_date', '2022-04-04 11:35:32.148208'),
(127, 'admin', '0014_holidays', '2022-04-12 03:44:49.894996'),
(128, 'applicants', '0017_alter_messages_date', '2022-04-12 03:44:49.901001'),
(129, 'employees', '0046_attendance_holiday', '2022-04-12 03:44:49.929953'),
(130, 'applicants', '0018_alter_messages_date', '2022-04-30 14:11:39.178352');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0gox420tq40t8jixggcsin4lhj7t82n7', '.eJxVjDsOwjAQBe_iGln-bUwo6XMGa9dr4wCypTipEHeHSCmgfTPzXiLgtpaw9bSEmcVFaHH63QjjI9Ud8B3rrcnY6rrMJHdFHrTLqXF6Xg_376BgL9_aupwgQ-Q4eO0sWIWKgK1noNHhOadsoh68ZR-zAiJFI7E1mrQjn4x4fwDwdThP:1neq6a:Rk7BM_iSfuFBMfALd4T6RvNhIyGKDp5q2owScsiqsMs', '2022-04-28 03:25:12.235805'),
('1rm7ff5o78krds76n21bdm2x0341iusa', '.eJxVjDsOwjAQBe_iGln-bUwo6XMGa9dr4wCypTipEHeHSCmgfTPzXiLgtpaw9bSEmcVFaHH63QjjI9Ud8B3rrcnY6rrMJHdFHrTLqXF6Xg_376BgL9_aupwgQ-Q4eO0sWIWKgK1noNHhOadsoh68ZR-zAiJFI7E1mrQjn4x4fwDwdThP:1nogDh:sOPRt8dBDEanE8bKLRk05Wur4pBG7fIu8S3Pb1gdfQ4', '2022-05-25 06:53:13.151888'),
('7wravvgawyt5cj22k6gg1zithopgpfgi', '.eJxVjDsOwjAQBe_iGln-bUwo6XMGa9dr4wCypTipEHeHSCmgfTPzXiLgtpaw9bSEmcVFaHH63QjjI9Ud8B3rrcnY6rrMJHdFHrTLqXF6Xg_376BgL9_aupwgQ-Q4eO0sWIWKgK1noNHhOadsoh68ZR-zAiJFI7E1mrQjn4x4fwDwdThP:1nof1i:r8VLgLAEdV73n6OT-Q5xqMFAMoOP1G0aTGWT231rv_A', '2022-05-25 05:36:46.206510'),
('8sclelilsf0ddo9ok8rdvsoko7x9n85y', '.eJxVjDsOwyAQBe9CHSHAmE_K9D4DWtglOImwZOwqyt2DJRdJOzPvvVmAfSthb7SGGdmVSXb5ZRHSk-oh8AH1vvC01G2dIz8SftrGpwXpdTvbv4MCrfR1csKBohHQRbTJoCVAmQcjvQJDgzJaCmv0mLSPWcXosyAhdSfQeWafL_HnN80:1nZxa7:7sDFw7kZpSOAWzv6V7Zv4-tzmSalGnn2-9t41kOu0ZQ', '2022-04-14 16:23:31.539044'),
('h99ewjsgtpe6yu86v98qero808x7edn0', '.eJxVjDsOwjAQBe_iGln-bUwo6XMGa9dr4wCypTipEHeHSCmgfTPzXiLgtpaw9bSEmcVFaHH63QjjI9Ud8B3rrcnY6rrMJHdFHrTLqXF6Xg_376BgL9_aupwgQ-Q4eO0sWIWKgK1noNHhOadsoh68ZR-zAiJFI7E1mrQjn4x4fwDwdThP:1pjf7f:x80wICBEazoUxC52BWGOPOr8hjOof5VcM5gJeZLcSrE', '2023-04-18 11:46:47.523007'),
('mg0fgpwqbitev1lgg34excu4jzemkoxb', '.eJxVjDsOwyAQBe9CHSHAmE_K9D4DWtglOImwZOwqyt2DJRdJOzPvvVmAfSthb7SGGdmVSXb5ZRHSk-oh8AH1vvC01G2dIz8SftrGpwXpdTvbv4MCrfR1csKBohHQRbTJoCVAmQcjvQJDgzJaCmv0mLSPWcXosyAhdSfQeWafL_HnN80:1piHbx:ISRSwGexTb9gWZIuu5bLKLLjDbexSaZ8qrITqGRFnio', '2023-04-14 16:28:21.065780'),
('oyz2zlxlm5nw5ure8k4k2fm77i2j2rrt', '.eJxVjDsOwyAQBe9CHSHAmE_K9D4DWtglOImwZOwqyt2DJRdJOzPvvVmAfSthb7SGGdmVSXb5ZRHSk-oh8AH1vvC01G2dIz8SftrGpwXpdTvbv4MCrfR1csKBohHQRbTJoCVAmQcjvQJDgzJaCmv0mLSPWcXosyAhdSfQeWafL_HnN80:1nw3bQ:IKzfG6aDPbkq8jiuJb1pMqHMBmMgJd2LWRcC73d1aZI', '2022-06-14 15:16:12.226356'),
('vld5ybxk6r83jkhjtu6ypkyyywhx86pm', '.eJxVjDsOwyAQBe9CHSHAmE_K9D4DWtglOImwZOwqyt2DJRdJOzPvvVmAfSthb7SGGdmVSXb5ZRHSk-oh8AH1vvC01G2dIz8SftrGpwXpdTvbv4MCrfR1csKBohHQRbTJoCVAmQcjvQJDgzJaCmv0mLSPWcXosyAhdSfQeWafL_HnN80:1lyU2B:RzguoXnM-gpNuqDv10SFAG5m2Qfwof7w1VMCHAB0ZoE', '2021-07-14 06:49:19.845054'),
('wrwecyyb7gn5ah6z7ueik1amos8lfqea', '.eJxVjDsOwjAQBe_iGln-bUwo6XMGa9dr4wCypTipEHeHSCmgfTPzXiLgtpaw9bSEmcVFaHH63QjjI9Ud8B3rrcnY6rrMJHdFHrTLqXF6Xg_376BgL9_aupwgQ-Q4eO0sWIWKgK1noNHhOadsoh68ZR-zAiJFI7E1mrQjn4x4fwDwdThP:1nbJrk:JlCA0o-u7u9QJ90EVWWTRAq8rj4DfYlAyZhl3JJkJbM', '2022-04-18 10:23:20.511611');

-- --------------------------------------------------------

--
-- Table structure for table `employees_attendance`
--

CREATE TABLE `employees_attendance` (
  `id` bigint(20) NOT NULL,
  `attendance_date` date NOT NULL,
  `entry_time` time(6) DEFAULT NULL,
  `exit_time` time(6) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  `shift` varchar(10) NOT NULL,
  `leave` tinyint(1) NOT NULL,
  `holiday` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employees_attendance`
--

INSERT INTO `employees_attendance` (`id`, `attendance_date`, `entry_time`, `exit_time`, `user_id`, `shift`, `leave`, `holiday`) VALUES
(11, '2022-04-01', '09:00:00.000000', '17:00:00.000000', 2, 'morning', 0, 0),
(12, '2022-04-01', NULL, NULL, 3, 'morning', 1, 0),
(13, '2022-04-01', '09:00:23.000000', '17:18:00.000000', 5, 'morning', 1, 0),
(14, '2022-04-01', NULL, NULL, 9, 'morning', 1, 0),
(16, '2022-04-01', '11:08:00.370561', '11:08:00.990302', 2, 'night', 0, 0),
(21, '2022-04-01', '18:30:00.000000', '01:30:00.000000', 5, 'night', 0, 0),
(23, '2022-04-02', '11:09:10.000000', '17:30:00.000000', 2, 'morning', 0, 0),
(24, '2022-04-02', NULL, NULL, 3, 'morning', 1, 0),
(25, '2022-04-02', NULL, NULL, 5, 'morning', 1, 0),
(26, '2022-04-02', NULL, NULL, 9, 'morning', 1, 0),
(30, '2022-04-02', '16:13:00.000000', '18:13:00.000000', 3, 'night', 0, 0),
(31, '2022-04-02', NULL, NULL, 12, 'morning', 1, 0),
(32, '2022-04-03', NULL, NULL, 2, 'morning', 0, 0),
(33, '2022-04-03', NULL, NULL, 3, 'morning', 0, 0),
(34, '2022-04-03', NULL, NULL, 5, 'morning', 0, 0),
(35, '2022-04-03', NULL, NULL, 9, 'morning', 0, 0),
(36, '2022-04-03', NULL, NULL, 12, 'morning', 0, 0),
(37, '2022-04-04', '11:42:00.000000', '14:42:00.000000', 2, 'morning', 1, 0),
(38, '2022-04-04', NULL, NULL, 3, 'morning', 1, 0),
(39, '2022-04-04', NULL, NULL, 5, 'morning', 0, 0),
(40, '2022-04-04', NULL, NULL, 9, 'morning', 0, 0),
(41, '2022-04-04', NULL, NULL, 12, 'morning', 0, 0),
(42, '2022-04-04', '10:42:13.526105', '10:42:14.326148', 2, 'night', 0, 0),
(43, '2022-04-04', '13:00:12.067117', '13:00:17.740451', 15, 'morning', 0, 0),
(44, '2022-04-05', NULL, NULL, 2, 'morning', 0, 0),
(45, '2022-04-05', NULL, NULL, 3, 'morning', 1, 0),
(46, '2022-04-05', NULL, NULL, 5, 'morning', 0, 0),
(47, '2022-04-05', NULL, NULL, 9, 'morning', 0, 0),
(48, '2022-04-05', NULL, NULL, 12, 'morning', 0, 0),
(49, '2022-04-05', NULL, NULL, 15, 'morning', 1, 0),
(50, '2022-04-07', '16:25:11.590323', '16:25:13.970167', 2, 'morning', 0, 0),
(51, '2022-04-07', NULL, NULL, 3, 'morning', 0, 0),
(52, '2022-04-07', NULL, NULL, 5, 'morning', 0, 0),
(53, '2022-04-07', NULL, NULL, 9, 'morning', 0, 0),
(54, '2022-04-07', NULL, NULL, 12, 'morning', 0, 0),
(55, '2022-04-07', NULL, NULL, 15, 'morning', 1, 0),
(56, '2022-04-08', NULL, NULL, 2, 'morning', 0, 0),
(57, '2022-04-08', NULL, NULL, 3, 'morning', 0, 0),
(58, '2022-04-08', NULL, NULL, 5, 'morning', 0, 0),
(59, '2022-04-08', NULL, NULL, 9, 'morning', 0, 0),
(60, '2022-04-08', NULL, NULL, 12, 'morning', 0, 0),
(61, '2022-04-08', NULL, NULL, 15, 'morning', 1, 0),
(62, '2022-04-09', '09:16:00.000000', '17:09:00.000000', 2, 'morning', 0, 0),
(63, '2022-04-09', '15:13:29.528726', '15:13:44.726329', 3, 'morning', 0, 0),
(64, '2022-04-09', NULL, NULL, 5, 'morning', 0, 0),
(65, '2022-04-09', NULL, NULL, 9, 'morning', 0, 0),
(66, '2022-04-09', NULL, NULL, 12, 'morning', 0, 0),
(67, '2022-04-09', NULL, NULL, 15, 'morning', 1, 0),
(70, '2022-04-09', '19:14:45.400154', '19:14:57.064751', 2, 'night', 0, 0),
(113, '2022-04-12', '09:27:00.000000', '17:02:00.000000', 2, 'morning', 0, 0),
(114, '2022-04-12', '20:44:14.999720', '20:44:15.575580', 3, 'morning', 0, 0),
(115, '2022-04-12', NULL, NULL, 5, 'morning', 1, 0),
(116, '2022-04-12', NULL, NULL, 9, 'morning', 0, 0),
(117, '2022-04-12', NULL, NULL, 12, 'morning', 0, 0),
(118, '2022-04-12', NULL, NULL, 15, 'morning', 1, 0),
(122, '2022-04-12', '11:46:42.130031', '11:46:44.585887', 2, 'night', 0, 0),
(123, '2022-04-13', '10:15:57.021918', '10:15:58.058508', 2, 'morning', 0, 0),
(124, '2022-04-13', '10:18:41.302690', '10:18:42.342914', 3, 'morning', 0, 0),
(125, '2022-04-13', '16:14:59.292670', '16:14:59.933431', 5, 'morning', 0, 0),
(126, '2022-04-13', '16:23:02.139992', '16:23:02.955896', 9, 'morning', 0, 0),
(127, '2022-04-13', '16:14:47.261327', '16:14:48.021380', 12, 'morning', 0, 0),
(128, '2022-04-13', NULL, NULL, 15, 'morning', 1, 0),
(129, '2022-04-14', NULL, NULL, 2, 'morning', 0, 1),
(130, '2022-04-14', NULL, NULL, 3, 'morning', 0, 1),
(131, '2022-04-14', NULL, NULL, 5, 'morning', 0, 1),
(132, '2022-04-14', NULL, NULL, 9, 'morning', 0, 1),
(133, '2022-04-14', NULL, NULL, 12, 'morning', 0, 1),
(134, '2022-04-14', NULL, NULL, 15, 'morning', 1, 1),
(135, '2022-04-16', '08:54:18.160487', '08:54:19.057617', 2, 'morning', 0, 0),
(136, '2022-04-16', '08:54:30.993384', '08:54:31.655905', 3, 'morning', 0, 0),
(137, '2022-04-16', NULL, NULL, 5, 'morning', 0, 0),
(138, '2022-04-16', NULL, NULL, 9, 'morning', 0, 0),
(139, '2022-04-16', '08:55:06.842446', '08:55:07.377807', 12, 'morning', 0, 0),
(140, '2022-04-16', NULL, NULL, 15, 'morning', 0, 0),
(141, '2022-04-18', '17:11:58.885299', '17:12:01.539524', 2, 'morning', 0, 0),
(142, '2022-04-18', '18:30:56.090561', '18:30:56.647048', 3, 'morning', 0, 0),
(143, '2022-04-18', NULL, NULL, 5, 'morning', 0, 0),
(144, '2022-04-18', NULL, NULL, 9, 'morning', 0, 0),
(145, '2022-04-18', NULL, NULL, 12, 'morning', 0, 0),
(146, '2022-04-18', NULL, NULL, 15, 'morning', 1, 0),
(147, '2022-04-19', '19:16:35.288760', '19:16:35.808965', 2, 'morning', 0, 0),
(148, '2022-04-19', '19:16:54.540499', '19:16:57.482526', 3, 'morning', 0, 0),
(149, '2022-04-19', NULL, NULL, 5, 'morning', 0, 0),
(150, '2022-04-19', NULL, NULL, 9, 'morning', 0, 0),
(151, '2022-04-19', NULL, NULL, 12, 'morning', 0, 0),
(152, '2022-04-19', NULL, NULL, 15, 'morning', 0, 0),
(153, '2022-04-21', '15:45:05.401708', '15:45:13.886871', 2, 'morning', 0, 0),
(154, '2022-04-21', NULL, NULL, 3, 'morning', 0, 0),
(155, '2022-04-21', NULL, NULL, 5, 'morning', 0, 0),
(156, '2022-04-21', NULL, NULL, 9, 'morning', 0, 0),
(157, '2022-04-21', NULL, NULL, 12, 'morning', 0, 0),
(158, '2022-04-21', NULL, NULL, 15, 'morning', 0, 0),
(159, '2022-04-22', '21:49:37.981888', '21:49:39.428271', 2, 'morning', 0, 0),
(160, '2022-04-22', '10:26:00.000000', '17:26:00.000000', 3, 'morning', 0, 0),
(161, '2022-04-22', NULL, NULL, 5, 'morning', 0, 0),
(162, '2022-04-22', NULL, NULL, 9, 'morning', 0, 0),
(163, '2022-04-22', NULL, NULL, 12, 'morning', 0, 0),
(164, '2022-04-22', NULL, NULL, 15, 'morning', 0, 0),
(165, '2022-04-23', '22:06:21.542652', '22:06:22.157673', 2, 'morning', 0, 0),
(166, '2022-04-23', NULL, NULL, 3, 'morning', 0, 0),
(167, '2022-04-23', NULL, NULL, 5, 'morning', 0, 0),
(168, '2022-04-23', NULL, NULL, 9, 'morning', 0, 0),
(169, '2022-04-23', NULL, NULL, 12, 'morning', 0, 0),
(170, '2022-04-23', NULL, NULL, 15, 'morning', 0, 0),
(171, '2022-04-24', NULL, NULL, 2, 'morning', 0, 1),
(172, '2022-04-24', NULL, NULL, 3, 'morning', 0, 1),
(173, '2022-04-24', NULL, NULL, 5, 'morning', 0, 1),
(174, '2022-04-24', NULL, NULL, 9, 'morning', 0, 1),
(175, '2022-04-24', NULL, NULL, 12, 'morning', 0, 1),
(176, '2022-04-24', NULL, NULL, 15, 'morning', 0, 1),
(177, '2022-04-25', NULL, NULL, 2, 'morning', 0, 0),
(178, '2022-04-25', NULL, NULL, 3, 'morning', 0, 0),
(179, '2022-04-25', NULL, NULL, 5, 'morning', 0, 0),
(180, '2022-04-25', NULL, NULL, 9, 'morning', 0, 0),
(181, '2022-04-25', NULL, NULL, 12, 'morning', 0, 0),
(182, '2022-04-25', NULL, NULL, 15, 'morning', 0, 0),
(183, '2022-04-30', '17:46:40.726162', '17:46:41.317399', 2, 'morning', 0, 0),
(184, '2022-04-30', NULL, NULL, 3, 'morning', 0, 0),
(185, '2022-04-30', NULL, NULL, 5, 'morning', 0, 0),
(186, '2022-04-30', NULL, NULL, 9, 'morning', 0, 0),
(187, '2022-04-30', NULL, NULL, 12, 'morning', 0, 0),
(188, '2022-04-30', NULL, NULL, 15, 'morning', 0, 0),
(189, '2022-05-06', '10:25:10.572994', '10:25:16.717897', 2, 'morning', 0, 0),
(190, '2022-05-06', NULL, NULL, 3, 'morning', 0, 0),
(191, '2022-05-06', NULL, NULL, 5, 'morning', 0, 0),
(192, '2022-05-06', NULL, NULL, 9, 'morning', 0, 0),
(193, '2022-05-06', NULL, NULL, 12, 'morning', 0, 0),
(194, '2022-05-06', NULL, NULL, 15, 'morning', 0, 0),
(196, '2022-05-07', '12:14:32.827235', '12:14:33.306010', 2, 'morning', 0, 0),
(197, '2022-05-07', NULL, NULL, 3, 'morning', 0, 0),
(198, '2022-05-07', NULL, NULL, 5, 'morning', 0, 0),
(199, '2022-05-07', NULL, NULL, 9, 'morning', 0, 0),
(200, '2022-05-07', NULL, NULL, 12, 'morning', 0, 0),
(201, '2022-05-07', NULL, NULL, 15, 'morning', 0, 0),
(203, '2022-05-10', NULL, NULL, 2, 'morning', 0, 0),
(204, '2022-05-10', NULL, NULL, 3, 'morning', 0, 0),
(205, '2022-05-10', NULL, NULL, 5, 'morning', 0, 0),
(206, '2022-05-10', NULL, NULL, 9, 'morning', 0, 0),
(207, '2022-05-10', NULL, NULL, 12, 'morning', 0, 0),
(208, '2022-05-10', NULL, NULL, 15, 'morning', 0, 0),
(210, '2022-05-11', '11:06:16.739820', '11:06:17.693859', 2, 'morning', 0, 0),
(211, '2022-05-11', NULL, NULL, 3, 'morning', 0, 0),
(212, '2022-05-11', NULL, NULL, 5, 'morning', 0, 0),
(213, '2022-05-11', NULL, NULL, 9, 'morning', 0, 0),
(214, '2022-05-11', NULL, NULL, 12, 'morning', 0, 0),
(215, '2022-05-11', NULL, NULL, 15, 'morning', 0, 0),
(216, '2022-05-15', '20:40:26.685396', '20:40:27.350263', 2, 'morning', 0, 1),
(217, '2022-05-15', NULL, NULL, 3, 'morning', 0, 1),
(218, '2022-05-15', NULL, NULL, 5, 'morning', 0, 1),
(219, '2022-05-15', NULL, NULL, 9, 'morning', 0, 1),
(220, '2022-05-15', NULL, NULL, 12, 'morning', 0, 1),
(221, '2022-05-15', NULL, NULL, 15, 'morning', 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `employees_attendanceregularization`
--

CREATE TABLE `employees_attendanceregularization` (
  `id` bigint(20) NOT NULL,
  `date` date NOT NULL,
  `old_entry` time(6) NOT NULL,
  `new_entry` time(6) NOT NULL,
  `old_exit` time(6) NOT NULL,
  `new_exit` time(6) NOT NULL,
  `reason` longtext NOT NULL,
  `status` varchar(12) NOT NULL,
  `attendance_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `shift` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employees_attendanceregularization`
--

INSERT INTO `employees_attendanceregularization` (`id`, `date`, `old_entry`, `new_entry`, `old_exit`, `new_exit`, `reason`, `status`, `attendance_id`, `user_id`, `shift`) VALUES
(6, '2022-04-01', '11:03:52.200221', '09:00:00.000000', '11:04:01.038233', '17:00:00.000000', 'Forgot to mark', 'approved', 11, 2, 'morning'),
(7, '2022-04-01', '18:54:27.000000', '18:30:00.000000', '00:00:00.000000', '01:30:00.000000', 'Forgot to mark', 'rejected', 21, 5, 'night'),
(8, '2022-04-04', '10:41:55.668911', '11:42:00.000000', '10:41:57.123600', '14:42:00.000000', 'Forgot to mark', 'approved', 37, 2, 'morning'),
(9, '2022-04-07', '16:25:11.590323', '10:15:00.000000', '16:25:13.970167', '15:55:00.000000', 'Forgot to mark', 'rejected', 50, 2, 'morning'),
(10, '2022-04-09', '09:50:34.926087', '09:16:00.000000', '09:50:35.967879', '17:09:00.000000', 'Technical Error', 'approved', 62, 2, 'morning'),
(12, '2022-04-12', '11:22:43.682429', '09:27:00.000000', '11:22:44.577912', '17:02:00.000000', 'Forgot to mark', 'approved', 113, 2, 'morning'),
(13, '2022-04-13', '16:14:47.261327', '10:16:00.000000', '16:14:48.021380', '17:19:00.000000', 'Forgot to mark', 'rejected', 127, 12, 'morning'),
(14, '2022-04-22', '21:50:27.293151', '10:26:00.000000', '21:50:27.996945', '17:26:00.000000', 'Forgot to mark', 'approved', 160, 3, 'morning'),
(15, '2022-04-30', '17:46:40.726162', '09:00:00.000000', '17:46:41.317399', '17:48:00.000000', 'Device error', 'pending', 183, 2, 'morning'),
(16, '2022-05-06', '10:25:10.572994', '10:41:00.000000', '10:25:16.717897', '17:41:00.000000', 'Forgot to mark', 'pending', 189, 2, 'morning');

-- --------------------------------------------------------

--
-- Table structure for table `employees_employeedesignation`
--

CREATE TABLE `employees_employeedesignation` (
  `id` bigint(20) NOT NULL,
  `department_id` bigint(20) NOT NULL,
  `designation_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employees_employeedesignation`
--

INSERT INTO `employees_employeedesignation` (`id`, `department_id`, `designation_id`, `user_id`) VALUES
(1, 1, 1, 2),
(2, 3, 2, 3),
(3, 1, 3, 5),
(4, 1, 4, 9),
(7, 1, 3, 12),
(8, 3, 5, 15);

-- --------------------------------------------------------

--
-- Table structure for table `employees_employeeprofile`
--

CREATE TABLE `employees_employeeprofile` (
  `id` bigint(20) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `dob` date DEFAULT NULL,
  `addressline1` varchar(60) NOT NULL,
  `place` varchar(60) NOT NULL,
  `city` varchar(60) NOT NULL,
  `state` varchar(60) NOT NULL,
  `pin` varchar(6) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employees_employeeprofile`
--

INSERT INTO `employees_employeeprofile` (`id`, `gender`, `dob`, `addressline1`, `place`, `city`, `state`, `pin`, `phone`, `photo`, `user_id`) VALUES
(1, 'Male', '2000-11-13', 'Puliyanakunnel (H)', 'Ezhumuttom', 'Thodupuzha', 'Kerala', '685605', '9876543210', 'team-1.jpg', 2),
(2, 'Male', '2022-03-26', 'Puliyanakunnel (H)', 'Ezhumuttom', 'Thodupuzha', 'Kerala', '685605', '8281074282', 'team-3.jpg', 3),
(3, 'Male', '2001-06-13', 'AbcdHouse (H)      ', 'Muvattupuzha      ', 'Muvattupuzha      ', 'Kerala      ', '685605', '8281074245', 'avatar-20.jpg', 5),
(4, 'Male', '1994-02-11', '9014 NE St Johns Rd', 'Vancouver', 'Vancouver', '	Washington', '555968', '7788996655', 'avatar-26.jpg', 9),
(6, 'Male', '1998-06-09', 'Something (H)', 'Thodupuzha', 'Thodupuzha', 'Kerala', '123455', '9638527410', 'avatar-02.jpg', 12),
(7, 'Male', '2000-06-20', 'pallickamayalil', 'thodupuzha', 'Thodupuzha', 'Kerala', '685588', '9207140729', 'avatar-09.jpg', 15);

-- --------------------------------------------------------

--
-- Table structure for table `employees_leave`
--

CREATE TABLE `employees_leave` (
  `id` bigint(20) NOT NULL,
  `leave_type` varchar(20) NOT NULL,
  `reason` longtext NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `from_date` date NOT NULL,
  `from_session` varchar(10) NOT NULL,
  `to_date` date NOT NULL,
  `to_session` varchar(10) NOT NULL,
  `approval` varchar(12) NOT NULL,
  `applied_date` datetime(6) NOT NULL,
  `attachments` varchar(100) NOT NULL,
  `admin` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employees_leave`
--

INSERT INTO `employees_leave` (`id`, `leave_type`, `reason`, `user_id`, `from_date`, `from_session`, `to_date`, `to_session`, `approval`, `applied_date`, `attachments`, `admin`) VALUES
(4, 'earned leave', 'Hospital', 2, '2022-04-04', 'session 1', '2022-04-04', 'session 2', 'approved', '2022-03-26 06:06:30.974403', '', 0),
(13, 'earned leave', 'First Leave', 5, '2022-04-01', 'session 1', '2022-04-01', 'session 2', 'approved', '2022-03-31 10:22:48.933717', '', 0),
(16, 'casual leave', 'New reason', 5, '2022-04-12', 'session 1', '2022-04-13', 'session 2', 'approved', '2022-03-31 12:46:03.138770', '', 0),
(17, 'casual leave', 'Test Leave Reason', 3, '2022-04-04', 'session 1', '2022-04-05', 'session 1', 'approved', '2022-03-31 12:49:31.689261', '', 0),
(20, 'earned leave', 'check leave', 3, '2022-04-01', 'session 1', '2022-04-01', 'session 2', 'approved', '2022-04-01 08:47:32.450182', '', 0),
(22, 'casual leave', 'Leave Added by admin', 9, '2022-04-01', 'session 1', '2022-04-01', 'session 2', 'approved', '2022-04-01 13:00:33.704617', '', 1),
(23, 'earned leave', 'Leave Added by admin', 9, '2022-04-02', 'session 1', '2022-04-02', 'session 2', 'approved', '2022-04-02 03:35:56.233506', '', 1),
(24, 'sick leave', 'Leave Added by admin', 5, '2022-04-02', 'session 1', '2022-04-02', 'session 2', 'approved', '2022-04-02 06:32:37.707784', '', 1),
(25, 'casual leave', 'Leave Added by admin', 3, '2022-04-02', 'session 1', '2022-04-02', 'session 2', 'approved', '2022-04-02 07:48:46.462301', '', 1),
(27, 'earned leave', 'Check reason', 12, '2022-04-29', 'session 1', '2022-05-01', 'session 1', 'approved', '2022-04-02 13:37:23.832620', '', 0),
(28, 'casual leave', 'Another Reason', 12, '2022-04-06', 'session 1', '2022-04-07', 'session 2', 'rejected', '2022-04-02 14:28:28.927611', '', 0),
(29, 'casual leave', 'Leave Added by admin', 12, '2022-04-02', 'session 1', '2022-04-02', 'session 2', 'approved', '2022-04-02 14:36:01.653680', '', 1),
(30, 'casual leave', 'reason', 2, '2022-04-13', 'session 1', '2022-04-13', 'session 2', 'approved', '2022-04-04 05:15:47.912471', '', 0),
(31, 'sick leave', 'chill', 15, '2022-04-04', 'session 1', '2022-04-14', 'session 2', 'approved', '2022-04-04 07:31:48.650491', '', 0),
(32, 'casual leave', 'No reason', 2, '2022-04-10', 'session 1', '2022-04-10', 'session 2', 'approved', '2022-04-09 04:49:03.269383', '', 0),
(34, 'sick leave', 'Hospital', 2, '2022-04-19', 'session 1', '2022-04-19', 'session 2', 'approved', '2022-04-09 05:50:11.488738', '', 0),
(35, 'casual leave', 'Test Leave', 2, '2022-04-28', 'session 1', '2022-04-28', 'session 2', 'approved', '2022-04-09 06:03:31.348424', '', 0),
(36, 'earned leave', 'test reason', 12, '2022-04-15', 'session 1', '2022-04-15', 'session 2', 'approved', '2022-04-09 10:29:36.853083', '', 0),
(37, 'sick leave', 'Hospital', 5, '2022-04-25', 'session 1', '2022-04-25', 'session 2', 'rejected', '2022-04-13 10:47:02.072228', '', 0),
(38, 'casual leave', 'Leave Added by admin', 15, '2022-04-18', 'session 1', '2022-04-18', 'session 2', 'approved', '2022-04-18 13:04:10.185294', '', 1);

-- --------------------------------------------------------

--
-- Table structure for table `employees_leavecounter`
--

CREATE TABLE `employees_leavecounter` (
  `id` bigint(20) NOT NULL,
  `cl` double NOT NULL,
  `el` double NOT NULL,
  `lp` double NOT NULL,
  `sl` double NOT NULL,
  `date` date NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employees_leavecounter`
--

INSERT INTO `employees_leavecounter` (`id`, `cl`, `el`, `lp`, `sl`, `date`, `user_id`) VALUES
(1, 0, 0, 0, 0, '2022-01-01', 2),
(2, 0, 0, 0, 0, '2022-01-01', 3),
(3, 0, 0, 0, 0, '2022-01-01', 5),
(4, 0, 0, 0, 0, '2022-01-01', 9),
(5, 0, 0, 0, 0, '2022-02-01', 2),
(6, 0, 0, 0, 0, '2022-02-01', 3),
(7, 0, 0, 0, 0, '2022-02-01', 5),
(8, 0, 0, 0, 0, '2022-02-01', 9),
(9, 0, 0, 0, 0, '2022-03-01', 2),
(10, 0, 0, 0, 0, '2022-03-01', 3),
(11, 0, 0, 0, 0, '2022-03-01', 5),
(12, 0, 0, 0, 0, '2022-03-01', 9),
(13, 3, 1, 0, 1, '2022-04-01', 2),
(14, 2.5, 1, 0, 0, '2022-04-01', 3),
(15, 2, 1, 0, 1, '2022-04-01', 5),
(16, 1, 1, 0, 0, '2022-04-01', 9),
(17, 0, 0, 0, 0, '2022-05-01', 2),
(18, 0, 0, 0, 0, '2022-05-01', 3),
(19, 0, 0, 0, 0, '2022-05-01', 5),
(20, 0, 0, 0, 0, '2022-05-01', 9),
(21, 0, 0, 0, 0, '2022-06-01', 2),
(22, 0, 0, 0, 0, '2022-06-01', 3),
(23, 0, 0, 0, 0, '2022-06-01', 5),
(24, 0, 0, 0, 0, '2022-06-01', 9),
(25, 0, 0, 0, 0, '2022-07-01', 2),
(26, 0, 0, 0, 0, '2022-07-01', 3),
(27, 0, 0, 0, 0, '2022-07-01', 5),
(28, 0, 0, 0, 0, '2022-07-01', 9),
(29, 0, 0, 0, 0, '2022-08-01', 2),
(30, 0, 0, 0, 0, '2022-08-01', 3),
(31, 0, 0, 0, 0, '2022-08-01', 5),
(32, 0, 0, 0, 0, '2022-08-01', 9),
(33, 0, 0, 0, 0, '2022-09-01', 2),
(34, 0, 0, 0, 0, '2022-09-01', 3),
(35, 0, 0, 0, 0, '2022-09-01', 5),
(36, 0, 0, 0, 0, '2022-09-01', 9),
(37, 0, 0, 0, 0, '2022-10-01', 2),
(38, 0, 0, 0, 0, '2022-10-01', 3),
(39, 0, 0, 0, 0, '2022-10-01', 5),
(40, 0, 0, 0, 0, '2022-10-01', 9),
(41, 0, 0, 0, 0, '2022-11-01', 2),
(42, 0, 0, 0, 0, '2022-11-01', 3),
(43, 0, 0, 0, 0, '2022-11-01', 5),
(44, 0, 0, 0, 0, '2022-11-01', 9),
(45, 0, 0, 0, 0, '2022-12-01', 2),
(46, 0, 0, 0, 0, '2022-12-01', 3),
(47, 0, 0, 0, 0, '2022-12-01', 5),
(48, 0, 0, 0, 0, '2022-12-01', 9),
(49, 0, 0, 0, 0, '2022-01-01', 12),
(50, 0, 0, 0, 0, '2022-02-01', 12),
(51, 0, 0, 0, 0, '2022-03-01', 12),
(52, 1, 3, 0, 0, '2022-04-01', 12),
(53, 0, 0.5, 0, 0, '2022-05-01', 12),
(54, 0, 0, 0, 0, '2022-06-01', 12),
(55, 0, 0, 0, 0, '2022-07-01', 12),
(56, 0, 0, 0, 0, '2022-08-01', 12),
(57, 0, 0, 0, 0, '2022-09-01', 12),
(58, 0, 0, 0, 0, '2022-10-01', 12),
(59, 0, 0, 0, 0, '2022-11-01', 12),
(60, 0, 0, 0, 0, '2022-12-01', 12),
(61, 0, 0, 0, 0, '2022-01-01', 15),
(62, 0, 0, 0, 0, '2022-02-01', 15),
(63, 0, 0, 0, 0, '2022-03-01', 15),
(64, 1, 0, 0, 11, '2022-04-01', 15),
(65, 0, 0, 0, 0, '2022-05-01', 15),
(66, 0, 0, 0, 0, '2022-06-01', 15),
(67, 0, 0, 0, 0, '2022-07-01', 15),
(68, 0, 0, 0, 0, '2022-08-01', 15),
(69, 0, 0, 0, 0, '2022-09-01', 15),
(70, 0, 0, 0, 0, '2022-10-01', 15),
(71, 0, 0, 0, 0, '2022-11-01', 15),
(72, 0, 0, 0, 0, '2022-12-01', 15);

-- --------------------------------------------------------

--
-- Table structure for table `employees_yearcounter`
--

CREATE TABLE `employees_yearcounter` (
  `id` bigint(20) NOT NULL,
  `cl` double NOT NULL,
  `el` double NOT NULL,
  `lp` double NOT NULL,
  `sl` double NOT NULL,
  `date` date NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employees_yearcounter`
--

INSERT INTO `employees_yearcounter` (`id`, `cl`, `el`, `lp`, `sl`, `date`, `user_id`) VALUES
(1, 3, 1, 0, 1, '2022-03-31', 2),
(2, 2.5, 1, 0, 0, '2022-03-31', 3),
(3, 2, 1, 0, 1, '2022-03-31', 5),
(4, 1, 1, 0, 0, '2022-03-31', 9),
(14, 1, 3.5, 0, 0, '2022-04-02', 12),
(15, 1, 0, 0, 11, '2022-04-04', 15);

-- --------------------------------------------------------

--
-- Table structure for table `users_applicantprofile`
--

CREATE TABLE `users_applicantprofile` (
  `id` bigint(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `dob` date DEFAULT NULL,
  `place` varchar(60) NOT NULL,
  `city` varchar(60) NOT NULL,
  `state` varchar(60) NOT NULL,
  `pin` varchar(6) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `cv` varchar(100) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `last_apply` date DEFAULT NULL,
  `addressline1` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users_applicantprofile`
--

INSERT INTO `users_applicantprofile` (`id`, `gender`, `dob`, `place`, `city`, `state`, `pin`, `phone`, `cv`, `user_id`, `last_apply`, `addressline1`) VALUES
(1, 'Female', '2016-06-07', 'Ezhumuttom', 'Thodupuzha', 'Kerala', '685605', '8976543210', 'sample.pdf', 4, '2022-03-26', 'Puliyanakunnel (H)'),
(2, 'Male', '2022-03-24', 'Ezhumuttom', 'Thodupuzha', 'Kerala', '685605', '8281074288', 'sample_AjUdRQY.pdf', 6, '2022-03-26', 'Puliyanakunnel (H)'),
(3, 'Male', '1990-06-05', 'Kingston', 'Queensland', 'Queensland', '125489', '7887555562', 'sample_QBAzyh8.pdf', 7, '2022-03-29', 'Greenwood'),
(5, 'Male', '2022-02-08', 'Ezhumuttom', 'Thodupuzha', 'Kerala', '685605', '8281074283', 'sample_UNv8gxM.pdf', 13, NULL, 'Puliyanakunnel (H)'),
(6, 'Male', '2000-10-30', 'Vadattupara', 'Kothamangalam', 'Kerala', '686681', '8606623649', 'sample_81sQBI6.pdf', 14, NULL, 'Thekkilakattu (H)');

-- --------------------------------------------------------

--
-- Table structure for table `users_newuser`
--

CREATE TABLE `users_newuser` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `middle_name` varchar(60) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_applicant` tinyint(1) NOT NULL,
  `is_employee` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users_newuser`
--

INSERT INTO `users_newuser` (`id`, `password`, `last_login`, `is_superuser`, `first_name`, `last_name`, `is_staff`, `is_active`, `date_joined`, `middle_name`, `email`, `is_applicant`, `is_employee`) VALUES
(1, 'pbkdf2_sha256$260000$N5lOADfqm09FvHaMUtkibz$Jmi0VIq3kOZZL0uhGQX8yEBbzHaWtAHlCIz9kq1dYTk=', '2022-05-15 15:10:36.128516', 1, '', '', 1, 1, '2022-03-25 14:00:26.614015', '', 'admin@admin.com', 0, 0),
(2, 'pbkdf2_sha256$260000$WhCZopiFTcmaYpJtaMldOW$V+uI9L2mg9xapT2NGRrkMpxPW9Osed8x9iDeVrpOW+w=', '2022-05-15 15:10:12.567460', 0, 'jewel', 'mathew', 0, 1, '2022-03-25 14:09:37.532367', '', 'jewel@gmail.com', 0, 1),
(3, 'pbkdf2_sha256$260000$uROohsFagqKetBeBEebx5e$LPnLSfCyelXlUc7gJhwE4C324S8gtM371g9YL3SyFYc=', '2022-04-22 16:55:55.112439', 0, 'limesh', 'mathew', 0, 1, '2022-03-25 14:10:13.621418', 'p', 'limesh@gmail.com', 0, 1),
(4, 'pbkdf2_sha256$260000$Ms6b8yaIyx7TEUplo6vclB$sXqNeyiMdzMMzUwnD17nYvYyoMEv0rD/tHFGoZcUkMU=', '2022-04-19 13:57:30.095244', 0, 'lissy', 'mathew', 0, 1, '2022-03-26 08:05:51.140128', '', 'lissy@gmail.com', 1, 0),
(5, 'pbkdf2_sha256$260000$3P7bW9Le5Cr86tzBVHL3X5$g8OMYRHKro5M4cMoCf/Ram5BaZ6SxDgwwsDxjS8txj8=', '2022-04-16 03:46:36.656488', 0, 'Eldhose', 'Babu', 0, 1, '2022-03-26 09:24:49.811027', '', 'eldhose@gmail.com', 0, 1),
(6, 'pbkdf2_sha256$260000$Ci9q3l6hnZY8MDm3642weA$KPbdFGtbwUv5ouYJqYqNQ0TTZ7rlweR08q/AB8CR014=', '2022-05-11 06:51:22.624921', 0, 'mathew', 'mathew', 0, 1, '2022-03-26 10:55:14.727319', '', 'mathew@gmail.com', 1, 0),
(7, 'pbkdf2_sha256$260000$ounw5RycmMbgArTLjfExFu$cODR9tXO1RvkL5gQKSr8A3wcbfi+H9doHnL/mPkcgPI=', '2022-04-16 16:51:16.063555', 0, 'John', 'Carter', 0, 1, '2022-03-29 06:31:49.612003', '', 'john@gmail.com', 1, 0),
(9, 'pbkdf2_sha256$260000$enrrxKHvZEbgIREt3PGGHZ$gukSYsldivC66yJZGxXq0kpKctfN/hWHuLEg5yUmnZM=', '2022-04-13 10:52:49.710133', 0, 'Berry', 'Lockman', 0, 1, '2022-03-29 08:48:51.090231', '', 'berry@gmail.com', 0, 1),
(12, 'pbkdf2_sha256$260000$2h5Nyk8WUG2hqFStZBOG2i$6HJgcxUSwKpldbOo4Vq60Tn/ozKDbtPMZS95r2A5tOc=', '2022-04-16 03:46:57.095110', 0, 'Jerry', 'Joseph', 0, 1, '2022-04-02 13:16:42.939018', '', 'jerry@gmail.com', 0, 1),
(13, 'pbkdf2_sha256$260000$jYQQ0wwv0jNKdVwSXUCjsW$eWTRP4GMHSDGScXu351YyAxnOIkN6JNSzkXTAvfdUQI=', '2022-04-04 05:10:08.000165', 0, 'jo', 'jose', 0, 1, '2022-04-04 05:09:46.233486', '', 'joe@gmail.com', 1, 0),
(14, 'pbkdf2_sha256$260000$5cba7ovpMNJNbAKXQMFQ4x$sBOhYqa/dJLXrvyAdjzJsU8GA6w88pyL7qNv+5D+5Hw=', '2022-04-04 05:49:14.069893', 0, 'Abin', 'sibi', 0, 1, '2022-04-04 05:48:42.557198', '', 'abin@gmail.com', 1, 0),
(15, 'pbkdf2_sha256$260000$R90kMU8UxGp702FXeGzpKo$VxhlfmZyAUvebimjJ3q0G5jdQtPk0seVOTrl+4F+Tcw=', '2022-04-04 07:26:49.117635', 0, 'Ajal', 'jose', 0, 1, '2022-04-04 07:26:04.542016', '', 'ajaljose2000@gmail.com', 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `users_newuser_groups`
--

CREATE TABLE `users_newuser_groups` (
  `id` bigint(20) NOT NULL,
  `newuser_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users_newuser_user_permissions`
--

CREATE TABLE `users_newuser_user_permissions` (
  `id` bigint(20) NOT NULL,
  `newuser_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_designations`
--
ALTER TABLE `admin_designations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `admin_holidays`
--
ALTER TABLE `admin_holidays`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `admin_payroll`
--
ALTER TABLE `admin_payroll`
  ADD PRIMARY KEY (`id`),
  ADD KEY `admin_payroll_user_id_a09e380c_fk_users_newuser_id` (`user_id`);

--
-- Indexes for table `admin_salary`
--
ALTER TABLE `admin_salary`
  ADD PRIMARY KEY (`id`),
  ADD KEY `admin_salary_user_id_423def22_fk_users_newuser_id` (`user_id`);

--
-- Indexes for table `applicants_applications`
--
ALTER TABLE `applicants_applications`
  ADD PRIMARY KEY (`id`),
  ADD KEY `applicants_applications_job_id_fe0332ca_fk_base_jobs_id` (`job_id`),
  ADD KEY `applicants_applications_user_id_f1670c3a_fk_users_newuser_id` (`user_id`);

--
-- Indexes for table `applicants_interviews`
--
ALTER TABLE `applicants_interviews`
  ADD PRIMARY KEY (`id`),
  ADD KEY `applicants_interview_department_id_d26cf201_fk_base_depa` (`department_id`),
  ADD KEY `applicants_interviews_job_id_6c0a5aba_fk_base_jobs_id` (`job_id`);

--
-- Indexes for table `applicants_messages`
--
ALTER TABLE `applicants_messages`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `base_department`
--
ALTER TABLE `base_department`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `base_jobs`
--
ALTER TABLE `base_jobs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_jobs_department_id_203dbc12_fk_base_department_id` (`department_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `employees_attendance`
--
ALTER TABLE `employees_attendance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employees_attendance_user_id_845bf4dd_fk_users_newuser_id` (`user_id`);

--
-- Indexes for table `employees_attendanceregularization`
--
ALTER TABLE `employees_attendanceregularization`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employees_attendance_attendance_id_deeb6eb4_fk_employees` (`attendance_id`),
  ADD KEY `employees_attendance_user_id_7c198f1b_fk_users_new` (`user_id`);

--
-- Indexes for table `employees_employeedesignation`
--
ALTER TABLE `employees_employeedesignation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employees_employeede_department_id_f23a8b8f_fk_base_depa` (`department_id`),
  ADD KEY `employees_employeede_designation_id_9427b166_fk_admin_des` (`designation_id`),
  ADD KEY `employees_employeede_user_id_35147c1a_fk_users_new` (`user_id`);

--
-- Indexes for table `employees_employeeprofile`
--
ALTER TABLE `employees_employeeprofile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `employees_leave`
--
ALTER TABLE `employees_leave`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employees_leave_user_id_c8d09b66_fk_users_newuser_id` (`user_id`);

--
-- Indexes for table `employees_leavecounter`
--
ALTER TABLE `employees_leavecounter`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employees_leavecounter_user_id_6101c837_fk_users_newuser_id` (`user_id`);

--
-- Indexes for table `employees_yearcounter`
--
ALTER TABLE `employees_yearcounter`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employees_yearcounter_user_id_e6ddbc29_fk_users_newuser_id` (`user_id`);

--
-- Indexes for table `users_applicantprofile`
--
ALTER TABLE `users_applicantprofile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `users_newuser`
--
ALTER TABLE `users_newuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `users_newuser_groups`
--
ALTER TABLE `users_newuser_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_newuser_groups_newuser_id_group_id_df6b4b64_uniq` (`newuser_id`,`group_id`),
  ADD KEY `users_newuser_groups_group_id_525a4e68_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `users_newuser_user_permissions`
--
ALTER TABLE `users_newuser_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_newuser_user_permi_newuser_id_permission_id_5e320e13_uniq` (`newuser_id`,`permission_id`),
  ADD KEY `users_newuser_user_p_permission_id_72696cfa_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_designations`
--
ALTER TABLE `admin_designations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `admin_holidays`
--
ALTER TABLE `admin_holidays`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `admin_payroll`
--
ALTER TABLE `admin_payroll`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `admin_salary`
--
ALTER TABLE `admin_salary`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `applicants_applications`
--
ALTER TABLE `applicants_applications`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `applicants_interviews`
--
ALTER TABLE `applicants_interviews`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `applicants_messages`
--
ALTER TABLE `applicants_messages`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=117;

--
-- AUTO_INCREMENT for table `base_department`
--
ALTER TABLE `base_department`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `base_jobs`
--
ALTER TABLE `base_jobs`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=131;

--
-- AUTO_INCREMENT for table `employees_attendance`
--
ALTER TABLE `employees_attendance`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=222;

--
-- AUTO_INCREMENT for table `employees_attendanceregularization`
--
ALTER TABLE `employees_attendanceregularization`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `employees_employeedesignation`
--
ALTER TABLE `employees_employeedesignation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `employees_employeeprofile`
--
ALTER TABLE `employees_employeeprofile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `employees_leave`
--
ALTER TABLE `employees_leave`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT for table `employees_leavecounter`
--
ALTER TABLE `employees_leavecounter`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=109;

--
-- AUTO_INCREMENT for table `employees_yearcounter`
--
ALTER TABLE `employees_yearcounter`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `users_applicantprofile`
--
ALTER TABLE `users_applicantprofile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `users_newuser`
--
ALTER TABLE `users_newuser`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `users_newuser_groups`
--
ALTER TABLE `users_newuser_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_newuser_user_permissions`
--
ALTER TABLE `users_newuser_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin_payroll`
--
ALTER TABLE `admin_payroll`
  ADD CONSTRAINT `admin_payroll_user_id_a09e380c_fk_users_newuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_newuser` (`id`);

--
-- Constraints for table `admin_salary`
--
ALTER TABLE `admin_salary`
  ADD CONSTRAINT `admin_salary_user_id_423def22_fk_users_newuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_newuser` (`id`);

--
-- Constraints for table `applicants_applications`
--
ALTER TABLE `applicants_applications`
  ADD CONSTRAINT `applicants_applications_job_id_fe0332ca_fk_base_jobs_id` FOREIGN KEY (`job_id`) REFERENCES `base_jobs` (`id`),
  ADD CONSTRAINT `applicants_applications_user_id_f1670c3a_fk_users_newuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_newuser` (`id`);

--
-- Constraints for table `applicants_interviews`
--
ALTER TABLE `applicants_interviews`
  ADD CONSTRAINT `applicants_interview_department_id_d26cf201_fk_base_depa` FOREIGN KEY (`department_id`) REFERENCES `base_department` (`id`),
  ADD CONSTRAINT `applicants_interviews_job_id_6c0a5aba_fk_base_jobs_id` FOREIGN KEY (`job_id`) REFERENCES `base_jobs` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `base_jobs`
--
ALTER TABLE `base_jobs`
  ADD CONSTRAINT `base_jobs_department_id_203dbc12_fk_base_department_id` FOREIGN KEY (`department_id`) REFERENCES `base_department` (`id`);

--
-- Constraints for table `employees_attendance`
--
ALTER TABLE `employees_attendance`
  ADD CONSTRAINT `employees_attendance_user_id_845bf4dd_fk_users_newuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_newuser` (`id`);

--
-- Constraints for table `employees_attendanceregularization`
--
ALTER TABLE `employees_attendanceregularization`
  ADD CONSTRAINT `employees_attendance_attendance_id_deeb6eb4_fk_employees` FOREIGN KEY (`attendance_id`) REFERENCES `employees_attendance` (`id`),
  ADD CONSTRAINT `employees_attendance_user_id_7c198f1b_fk_users_new` FOREIGN KEY (`user_id`) REFERENCES `users_newuser` (`id`);

--
-- Constraints for table `employees_employeedesignation`
--
ALTER TABLE `employees_employeedesignation`
  ADD CONSTRAINT `employees_employeede_department_id_f23a8b8f_fk_base_depa` FOREIGN KEY (`department_id`) REFERENCES `base_department` (`id`),
  ADD CONSTRAINT `employees_employeede_designation_id_9427b166_fk_admin_des` FOREIGN KEY (`designation_id`) REFERENCES `admin_designations` (`id`),
  ADD CONSTRAINT `employees_employeede_user_id_35147c1a_fk_users_new` FOREIGN KEY (`user_id`) REFERENCES `users_newuser` (`id`);

--
-- Constraints for table `employees_employeeprofile`
--
ALTER TABLE `employees_employeeprofile`
  ADD CONSTRAINT `employees_employeeprofile_user_id_14de7e1f_fk_users_newuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_newuser` (`id`);

--
-- Constraints for table `employees_leave`
--
ALTER TABLE `employees_leave`
  ADD CONSTRAINT `employees_leave_user_id_c8d09b66_fk_users_newuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_newuser` (`id`);

--
-- Constraints for table `employees_leavecounter`
--
ALTER TABLE `employees_leavecounter`
  ADD CONSTRAINT `employees_leavecounter_user_id_6101c837_fk_users_newuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_newuser` (`id`);

--
-- Constraints for table `employees_yearcounter`
--
ALTER TABLE `employees_yearcounter`
  ADD CONSTRAINT `employees_yearcounter_user_id_e6ddbc29_fk_users_newuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_newuser` (`id`);

--
-- Constraints for table `users_applicantprofile`
--
ALTER TABLE `users_applicantprofile`
  ADD CONSTRAINT `users_applicantprofile_user_id_9b68190b_fk_users_newuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_newuser` (`id`);

--
-- Constraints for table `users_newuser_groups`
--
ALTER TABLE `users_newuser_groups`
  ADD CONSTRAINT `users_newuser_groups_group_id_525a4e68_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `users_newuser_groups_newuser_id_7f6f4c4c_fk_users_newuser_id` FOREIGN KEY (`newuser_id`) REFERENCES `users_newuser` (`id`);

--
-- Constraints for table `users_newuser_user_permissions`
--
ALTER TABLE `users_newuser_user_permissions`
  ADD CONSTRAINT `users_newuser_user_p_newuser_id_bb22b5b4_fk_users_new` FOREIGN KEY (`newuser_id`) REFERENCES `users_newuser` (`id`),
  ADD CONSTRAINT `users_newuser_user_p_permission_id_72696cfa_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
